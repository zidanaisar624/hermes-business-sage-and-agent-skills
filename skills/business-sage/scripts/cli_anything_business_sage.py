#!/usr/bin/env python3
"""
cli-anything-business-sage (`bsage`): Zero-MCP-Token Agent-Native CLI Harness for Business Sage.

- Role: Internet-researched S1 (BBA/FEB) & S2 (MBA/MM) Business, Financial Strategy & Indonesian
  UMKM/Tax Co-Pilot + Eternal-Student Empirical Research Loop.
- Ethics: Built with deep respect for business students, scholars, certified accountants/tax/legal
  practitioners, and human entrepreneurs — strictly an Advisory Co-Pilot, NEVER a replacement.
- Safety: NEVER touches or modifies any user's Hermes `config.yaml`, `provider`, `model`, or `SOUL.md`.
- Compatibility: HKUDS/CLI-Anything (`--json` + Stateful REPL), Hermes (#1), OpenClaw, ChatGPT & Claude.
"""

from __future__ import annotations

import argparse
import cmd
import hashlib
import json
import math
import os
import platform
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.request
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

VERSION = "2.0.0"
DEFAULT_GITHUB_OWNER = "zidanaisar624"
DEFAULT_GITHUB_REPO = "hermes-business-sage-and-agent-skills"
DEFAULT_BRANCH = "main"
INSTALL_STATE_DIR_NAME = "business-sage-cli"

ADVISORY_ROLE_STATEMENT = (
    "Internet-Researched S1-S2 Business & Financial Co-Pilot + Eternal-Student Research Loop "
    "(Respecting Business Students, Certified Practitioners & Human Entrepreneurs — NOT a replacement)"
)

SKIP_DIRS_LOWER: Set[str] = {
    "$recycle.bin",
    "system volume information",
    "windows",
    "windowsapps",
    "wpsystem",
    "wudownloadcache",
    "program files",
    "program files (x86)",
    "programdata",
    "perflogs",
    "recovery",
    "msocache",
    "node_modules",
    ".git",
    ".hg",
    ".svn",
    "__pycache__",
    ".venv",
    "venv",
    "env",
    "hf-cache",
    "npm-cache",
    "pip-cache",
    "cache",
    "caches",
    "temp",
    "tmp",
    "steamlibrary",
    "xboxgames",
    "epic games",
    "onedrive",
    "googledrive",
    "library",
    "proc",
    "sys",
    "dev",
    "run",
    "snap",
}


# ==============================================================================
# 1. REPOSITORY, STATE & MULTI-DRIVE HERMES / MULTI-AGENT AUTO-DISCOVERY
# ==============================================================================

def resolve_repo_root(explicit: Optional[str] = None) -> Optional[Path]:
    if explicit:
        p = Path(explicit).expanduser().resolve()
        if p.is_dir():
            return p
    env_repo = os.environ.get("BSAGE_REPO")
    if env_repo:
        p = Path(env_repo).expanduser().resolve()
        if p.is_dir():
            return p
    here = Path(__file__).resolve()
    for parent in [here.parent] + list(here.parents):
        if (parent / "skills" / "business-sage" / "SKILL.md").is_file():
            return parent
    return None


def get_state_dir(explicit: Optional[str] = None) -> Path:
    base = Path(
        explicit
        or os.environ.get("BUSINESS_SAGE_HOME")
        or (Path.home() / ".business-sage")
    ).expanduser()
    (base / "phd_business_ledger").mkdir(parents=True, exist_ok=True)
    return base


def load_session(state_dir: Optional[Path] = None) -> Dict[str, Any]:
    sdir = state_dir or get_state_dir()
    path = sdir / "session.json"
    if path.is_file():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                data["advisor_role"] = ADVISORY_ROLE_STATEMENT
                return data
        except Exception:
            pass
    return {
        "version": VERSION,
        "advisor_role": ADVISORY_ROLE_STATEMENT,
        "phd_level": "Eternal Business Student (Empirical Research & Scenario Co-Pilot)",
        "history": [],
        "learned_insights": [],
    }


def save_session(state: Dict[str, Any], state_dir: Optional[Path] = None) -> None:
    sdir = state_dir or get_state_dir()
    sdir.mkdir(parents=True, exist_ok=True)
    (sdir / "session.json").write_text(
        json.dumps(state, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def is_hermes_home(path: Path) -> bool:
    try:
        if not path.is_dir():
            return False
        cfg_markers = (
            (path / "config.yaml").is_file(),
            (path / "profile.yaml").is_file(),
            (path / "SOUL.md").is_file(),
            (path / "state.db").is_file(),
            (path / ".skills_prompt_snapshot.json").is_file(),
        )
        dir_markers = (
            (path / "skills").is_dir(),
            (path / "profiles").is_dir(),
            (path / "memories").is_dir(),
            (path / "hermes-agent").is_dir(),
            (path / "sessions").is_dir(),
        )
        if any(cfg_markers) and any(dir_markers):
            return True
        if path.name.lower() in {".hermes", "hermesdata"} and (any(cfg_markers) or any(dir_markers)):
            return True
    except OSError:
        return False
    return False


def _resolve_hermes_fleet_root(home: Path) -> Path:
    try:
        lexical = Path(os.path.abspath(str(home)))
        if lexical.parent.name.lower() == "profiles" and is_hermes_home(lexical.parent.parent):
            return lexical.parent.parent
    except OSError:
        pass
    return home


def _list_hermes_profiles(root: Path) -> List[Path]:
    prof_dir = root / "profiles"
    out: List[Path] = []
    try:
        if not prof_dir.is_dir():
            return out
        for child in sorted(prof_dir.iterdir(), key=lambda p: p.name.lower()):
            if child.name.startswith("."):
                continue
            if is_hermes_home(child) or (child / "config.yaml").is_file() or (child / "SOUL.md").is_file():
                out.append(child)
    except OSError:
        pass
    return out


def _windows_registry_env_vars() -> Dict[str, str]:
    found: Dict[str, str] = {}
    if platform.system() != "Windows":
        return found
    try:
        import winreg  # type: ignore

        for hive, subkey in (
            (winreg.HKEY_CURRENT_USER, r"Environment"),
            (winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment"),
        ):
            try:
                with winreg.OpenKey(hive, subkey) as key:
                    idx = 0
                    while True:
                        try:
                            name, val, _ = winreg.EnumValue(key, idx)
                            idx += 1
                            if isinstance(val, str) and ("HERMES" in name.upper() or "OPENCLAW" in name.upper()):
                                found.setdefault(name, os.path.expandvars(val))
                        except OSError:
                            break
            except OSError:
                continue
    except Exception:
        pass
    return found


def _mounted_roots() -> List[Path]:
    roots: List[Path] = []
    if platform.system() == "Windows":
        for letter in "CDEFGHIJKLMNOPQRSTUVWXYZ":
            drv = Path(f"{letter}:\\")
            try:
                if drv.exists():
                    roots.append(drv)
            except OSError:
                continue
    else:
        for base in (Path("/mnt"), Path("/Volumes"), Path("/media"), Path("/run/media"), Path("/opt"), Path("/data")):
            try:
                if base.is_dir():
                    for child in sorted(base.iterdir()):
                        if child.is_dir():
                            roots.append(child)
            except OSError:
                continue
        roots.append(Path("/"))
    return roots


def _bounded_drive_scan(roots: List[Path], max_depth: int = 3, max_dirs_per_drive: int = 600) -> List[Path]:
    discovered: List[Path] = []
    seen: Set[str] = set()
    for root in roots:
        for rel in ("HermesData", "Hermes", ".hermes", "hermes-data", "HermesAgent", "AI/HermesData", "AI/Hermes"):
            cand = root / rel
            try:
                if is_hermes_home(cand):
                    norm = os.path.normcase(os.path.abspath(str(cand)))
                    if norm not in seen:
                        seen.add(norm)
                        discovered.append(cand)
            except OSError:
                continue

        queue: List[Tuple[Path, int]] = [(root, 0)]
        inspected = 0
        while queue and inspected < max_dirs_per_drive:
            current, depth = queue.pop(0)
            if depth >= max_depth:
                continue
            try:
                with os.scandir(current) as it:
                    for entry in it:
                        inspected += 1
                        if inspected > max_dirs_per_drive:
                            break
                        try:
                            if not entry.is_dir(follow_symlinks=False):
                                continue
                        except OSError:
                            continue
                        name_low = entry.name.lower()
                        if name_low in SKIP_DIRS_LOWER:
                            continue
                        if entry.name.startswith(".") and name_low != ".hermes":
                            continue
                        entry_path = Path(entry.path)
                        if "hermes" in name_low and is_hermes_home(entry_path):
                            root_cand = _resolve_hermes_fleet_root(entry_path)
                            norm = os.path.normcase(os.path.abspath(str(root_cand)))
                            if norm not in seen:
                                seen.add(norm)
                                discovered.append(root_cand)
                            continue
                        if depth + 1 < max_depth:
                            queue.append((entry_path, depth + 1))
            except OSError:
                continue
    return discovered


def discover_hermes_installations(deep_scan: bool = True, explicit_home: Optional[str] = None) -> List[Dict[str, Any]]:
    raw_candidates: List[Tuple[Path, str]] = []
    env_all = {**_windows_registry_env_vars(), **os.environ}

    if explicit_home:
        raw_candidates.append((Path(explicit_home).expanduser(), "cli-flag:--hermes-home"))
    for k in ("HERMES_HOME", "HERMES_DATA", "HERMES_ROOT"):
        if env_all.get(k):
            raw_candidates.append((Path(env_all[k]).expanduser(), f"env:{k}"))
    if env_all.get("HERMES_INSTALL_DIR"):
        raw_candidates.append((Path(env_all["HERMES_INSTALL_DIR"]).expanduser().parent, "env:HERMES_INSTALL_DIR-parent"))

    hermes_bin = shutil.which("hermes")
    if hermes_bin:
        bp = Path(hermes_bin).resolve()
        if bp.parent.name.lower() == "bin":
            raw_candidates.append((bp.parent.parent, "path:hermes-bin-parent"))

    home = Path.home()
    raw_candidates.append((home / ".hermes", "standard:~/.hermes"))
    if platform.system() == "Windows":
        if os.environ.get("LOCALAPPDATA"):
            raw_candidates.append((Path(os.environ["LOCALAPPDATA"]) / "hermes", "windows:LOCALAPPDATA"))
        if os.environ.get("APPDATA"):
            raw_candidates.append((Path(os.environ["APPDATA"]) / "hermes", "windows:APPDATA"))
    else:
        xdg = os.environ.get("XDG_DATA_HOME", str(home / ".local" / "share"))
        raw_candidates.append((Path(xdg) / "hermes", "xdg:XDG_DATA_HOME"))

    if deep_scan:
        for scanned in _bounded_drive_scan(_mounted_roots()):
            raw_candidates.append((scanned, "deep-drive-scan"))

    verified: List[Dict[str, Any]] = []
    seen: Set[str] = set()
    for cand, source in raw_candidates:
        try:
            fleet = _resolve_hermes_fleet_root(cand)
            norm = os.path.normcase(os.path.abspath(str(fleet)))
            if norm in seen:
                continue
            if source == "cli-flag:--hermes-home" or is_hermes_home(fleet):
                seen.add(norm)
                profiles = _list_hermes_profiles(fleet)
                verified.append(
                    {
                        "root": str(fleet),
                        "skills_dir": str(fleet / "skills"),
                        "discovery_source": source,
                        "profiles": [
                            {"name": p.name, "path": str(p), "skills_dir": str(p / "skills")}
                            for p in profiles
                        ],
                    }
                )
        except OSError:
            continue
    return verified


def discover_other_agents() -> List[Dict[str, Any]]:
    home = Path.home()
    env = os.environ
    specs = [
        ("openclaw", "OpenClaw Agent", Path(env["OPENCLAW_HOME"]).expanduser() if env.get("OPENCLAW_HOME") else home / ".openclaw"),
        ("claude", "Claude Code / Anthropic CLI", Path(env["CLAUDE_CONFIG_DIR"]).expanduser() if env.get("CLAUDE_CONFIG_DIR") else home / ".claude"),
        ("codex", "OpenAI Codex / ChatGPT CLI", Path(env["CODEX_HOME"]).expanduser() if env.get("CODEX_HOME") else home / ".codex"),
        ("agents_universal", "Universal AgentSkills Standard (~/.agents)", home / ".agents"),
        ("cursor", "Cursor AI Editor", home / ".cursor"),
    ]
    out: List[Dict[str, Any]] = []
    for aid, label, base in specs:
        try:
            out.append(
                {
                    "agent_id": aid,
                    "label": label,
                    "home": str(base),
                    "skills_dir": str(base / "skills"),
                    "detected": base.is_dir(),
                }
            )
        except OSError:
            continue
    return out


def discover_agent_skill_dirs(deep_scan: bool = True) -> List[str]:
    dirs: List[str] = []
    for h in discover_hermes_installations(deep_scan=deep_scan):
        dirs.append(str(h["skills_dir"]))
        for p in h["profiles"]:
            dirs.append(str(p["skills_dir"]))
    for ag in discover_other_agents():
        if ag["detected"]:
            dirs.append(str(ag["skills_dir"]))
    return dirs


# ==============================================================================
# 2. BUSINESS, FINANCIAL, INDONESIAN TAX & TREND SCENARIO CALCULATORS
# ==============================================================================

def cmd_literacy_audit(args: argparse.Namespace) -> Dict[str, Any]:
    income = float(args.monthly_after_tax_income)
    needs = float(args.monthly_needs)
    wants = float(args.monthly_wants)
    savings = float(args.monthly_savings)
    liquid_cash = float(args.liquid_emergency_cash)
    high_apr_debt = float(args.high_apr_debt)

    needs_pct = round((needs / income) * 100, 2) if income > 0 else 0.0
    wants_pct = round((wants / income) * 100, 2) if income > 0 else 0.0
    savings_pct = round((savings / income) * 100, 2) if income > 0 else 0.0
    emergency_months = round(liquid_cash / needs, 2) if needs > 0 else 99.0

    recs: List[str] = []
    if emergency_months < 3.0:
        recs.append(
            f"Prioritas 1: Bangun Dana Darurat likuid hingga minimal 3-6x biaya pokok "
            f"({3 * needs:,.0f} - {6 * needs:,.0f}). Saat ini baru {emergency_months} bulan."
        )
    if high_apr_debt > 0:
        recs.append(
            f"Prioritas 2: Lunasi utang berbunga tinggi ({high_apr_debt:,.0f}) dengan metode Avalanche "
            "(suku bunga tertinggi lebih dulu) sebelum mengalokasikan modal ke instrumen berisiko."
        )
    if needs_pct > 50:
        recs.append(
            f"Optimasi Needs: Porsi kebutuhan pokok ({needs_pct}%) melebihi patokan 50%. "
            "Audit pengeluaran rutin menggunakan Per-Unit Pricing."
        )
    if savings_pct < 20:
        recs.append(f"Tingkatkan Tabungan/Investasi: Porsi tabungan ({savings_pct}%) berada di bawah target 20%.")
    if not recs:
        recs.append("Fondasi kas & dana darurat sehat (siap mendiskusikan alokasi investasi atau ekspansi bisnis terukur).")

    return {
        "status": "ok",
        "command": "literacy-audit",
        "advisory_role": ADVISORY_ROLE_STATEMENT,
        "budget_50_30_20_breakdown": {
            "needs_pct": needs_pct,
            "wants_pct": wants_pct,
            "savings_pct": savings_pct,
            "target_rule": "50% Needs / 30% Wants / 20% Savings (illustrative benchmark)",
        },
        "emergency_runway_months": emergency_months,
        "ready_for_risk_investment": (emergency_months >= 3.0 and high_apr_debt == 0),
        "recommendations": recs,
    }


def cmd_unit_economics(args: argparse.Namespace) -> Dict[str, Any]:
    price = float(args.price)
    var_cost = float(args.variable_cost)
    fixed_cost = float(args.monthly_fixed_cost)
    cac = float(args.cac)
    churn = float(args.monthly_churn_rate)

    cm = price - var_cost
    cm_pct = round((cm / price) * 100, 2) if price > 0 else 0.0
    bep_units = math.ceil(fixed_cost / cm) if cm > 0 else None
    ltv = round(cm / churn, 2) if churn > 0 else round(cm * 24, 2)
    ltv_cac = round(ltv / cac, 2) if cac > 0 else 999.0
    payback_months = round(cac / cm, 2) if cm > 0 else 999.0

    verdict = "HEALTHY_SCALABLE" if (ltv_cac >= 3.0 and payback_months <= 12.0 and cm > 0) else "NEEDS_OPTIMIZATION"
    return {
        "status": "ok",
        "command": "unit-economics",
        "advisory_role": ADVISORY_ROLE_STATEMENT,
        "contribution_margin_per_unit": round(cm, 2),
        "contribution_margin_pct": cm_pct,
        "break_even_units_per_month": bep_units,
        "gross_margin_ltv": ltv,
        "cac": cac,
        "ltv_to_cac_ratio": ltv_cac,
        "cac_payback_months": payback_months,
        "verdict": verdict,
        "benchmark_notes": (
            "Scenario target: LTV:CAC >= 3.0x and CAC Payback <= 12 months "
            "(computed strictly on Contribution Margin after COGS & payment MDR, never gross revenue)."
        ),
    }


def cmd_valuation_dcf(args: argparse.Namespace) -> Dict[str, Any]:
    fcff = float(args.initial_fcff)
    g_stage1 = float(args.growth_rate_5yr)
    g_terminal = float(args.terminal_growth_rate)
    wacc = float(args.wacc)
    cash = float(args.cash)
    debt = float(args.debt)

    if wacc <= g_terminal:
        return {"status": "error", "error": "WACC must be strictly greater than terminal_growth_rate."}

    pv_flows = []
    curr = fcff
    for t in range(1, 6):
        curr = curr * (1.0 + g_stage1)
        pv = curr / ((1.0 + wacc) ** t)
        pv_flows.append({"year": t, "projected_fcff": round(curr, 2), "present_value": round(pv, 2)})

    sum_pv = sum(x["present_value"] for x in pv_flows)
    tv = (curr * (1.0 + g_terminal)) / (wacc - g_terminal)
    pv_tv = tv / ((1.0 + wacc) ** 5)
    ev = sum_pv + pv_tv
    eq_val = ev + cash - debt

    return {
        "status": "ok",
        "command": "valuation-dcf",
        "advisory_role": ADVISORY_ROLE_STATEMENT,
        "five_year_cashflows": pv_flows,
        "pv_of_5yr_fcff": round(sum_pv, 2),
        "terminal_value_year_5": round(tv, 2),
        "pv_of_terminal_value": round(pv_tv, 2),
        "enterprise_value": round(ev, 2),
        "equity_value": round(eq_val, 2),
        "disclaimer": "Scenario DCF sensitivity model — not an appraisal or investment solicitation.",
    }


def cmd_indonesia_tax_legal(args: argparse.Namespace) -> Dict[str, Any]:
    omzet = float(args.annual_turnover_idr)
    net_profit = float(args.annual_net_profit_idr)
    entity = args.entity_type.lower()

    if omzet <= 2_000_000_000:
        scale = "Usaha Mikro (PP No. 7 Tahun 2021: Omzet <= Rp2 Miliar)"
        sak = "SAK EMKM (Ikatan Akuntan Indonesia)"
    elif omzet <= 15_000_000_000:
        scale = "Usaha Kecil (PP No. 7 Tahun 2021: Omzet >Rp2 Miliar s/d Rp15 Miliar)"
        sak = "SAK EMKM / SAK Entitas Privat (SAK EP)"
    elif omzet <= 50_000_000_000:
        scale = "Usaha Menengah (PP No. 7 Tahun 2021: Omzet >Rp15 Miliar s/d Rp50 Miliar)"
        sak = "SAK Entitas Privat (SAK EP)"
    else:
        scale = "Usaha Besar (Omzet > Rp50 Miliar)"
        sak = "SAK Indonesia (PSAK / Konvergensi IFRS)"

    if omzet <= 500_000_000:
        tax_op = 0.0
    elif omzet <= 4_800_000_000:
        tax_op = (omzet - 500_000_000) * 0.005
    else:
        tax_op = max(0.0, net_profit * 0.25)

    tax_pt_perorangan = omzet * 0.005 if omzet <= 4_800_000_000 else max(0.0, net_profit * 0.11)
    tax_koperasi = omzet * 0.005 if omzet <= 4_800_000_000 else max(0.0, net_profit * 0.11)

    if net_profit <= 0:
        tax_pt_biasa_or_cv = 0.0
    elif omzet <= 4_800_000_000:
        tax_pt_biasa_or_cv = net_profit * 0.11
    elif omzet <= 50_000_000_000:
        fasilitas_portion = (4_800_000_000 / omzet) * net_profit
        non_fasilitas = net_profit - fasilitas_portion
        tax_pt_biasa_or_cv = (fasilitas_portion * 0.11) + (non_fasilitas * 0.22)
    else:
        tax_pt_biasa_or_cv = net_profit * 0.22

    pkp_wajib = omzet > 4_800_000_000

    return {
        "status": "ok",
        "command": "indonesia-tax-legal",
        "advisory_role": ADVISORY_ROLE_STATEMENT,
        "selected_entity": entity,
        "umkm_scale_pp_7_2021": scale,
        "recommended_accounting_standard": sak,
        "mandatory_pkp_ppn": pkp_wajib,
        "tax_comparison_pp_20_2026_idr": {
            "wp_orang_pribadi_umkm": round(tax_op, 2),
            "pt_perorangan_umk": round(tax_pt_perorangan, 2),
            "koperasi_umkm_window": round(tax_koperasi, 2),
            "cv_atau_pt_biasa_pasal_31e": round(tax_pt_biasa_or_cv, 2),
        },
        "strategic_advisory": (
            "Ilustrasi skenario berdasarkan publikasi PP No. 20 Tahun 2026 & Pasal 31E UU PPh: "
            "(1) WP Orang Pribadi: Rp500 juta pertama 0%, sisanya s/d Rp4,8 Miliar tarif PPh Final 0,5% (perhatikan aturan agregasi omzet suami-istri & PT Perorangan); "
            "(2) PT Perorangan & Koperasi yang memenuhi syarat dapat memakai skema PPh Final 0,5% sesuai ketentuan masa berlaku; "
            "(3) CV & PT Biasa menggunakan PPh Badan Pasal 31E (efektif 11% dari Laba Bersih Fiskal s/d omzet Rp4,8 Miliar; Rp0 saat rugi fiskal). "
            "Selalu verifikasi fakta wajib pajak terkini bersama Konsultan Pajak Resmi (USKP) / DJP."
        ),
    }


def cmd_predict_trend(args: argparse.Namespace) -> Dict[str, Any]:
    sector = args.sector
    p = float(args.innovation_coeff_p)
    q = float(args.imitation_coeff_q)
    current_adoption = float(args.current_adoption_pct) / 100.0

    t_peak = round(math.log(q / p) / (p + q), 2) if (p > 0 and q > p) else 0.0
    instantaneous_velocity = (p + q * current_adoption) * (1.0 - current_adoption)

    if current_adoption < 0.025:
        phase = "Phase 1: Innovators (<2.5%) - High R&D risk, educate market via low-cost content & paid pilots."
    elif current_adoption <= 0.16:
        phase = "Phase 2: Golden Early-Adopter Inflection (2.5% - 16%) - OPTIMAL ENTRY WINDOW! Word-of-mouth (q) is accelerating while CAC is still low."
    elif current_adoption <= 0.50:
        phase = "Phase 3: Early Majority (16% - 50%) - Compete on specialized niche positioning, B2B picks-and-shovels, or Tier-2/3 geographic arbitrage."
    else:
        phase = "Phase 4: Late Majority / Saturation (>50%) - High CAC, margin compression; pivot to unbundling or cost-leadership."

    return {
        "status": "ok",
        "command": "predict-trend",
        "advisory_role": ADVISORY_ROLE_STATEMENT,
        "sector": sector,
        "bass_diffusion_metrics": {
            "p_innovation": p,
            "q_imitation": q,
            "current_adoption_pct": round(current_adoption * 100, 2),
            "years_to_peak_adoption_t_star": t_peak,
            "adoption_velocity_index": round(instantaneous_velocity * 100, 3),
        },
        "lifecycle_phase": phase,
        "profit_gap_arbitrage_angles": [
            f"Geo-Lag Arbitrage: Adapt proven US/China/Japan playbooks in '{sector}' for Indonesian Tier-1/Tier-2 cities with QRIS & WhatsApp consultative closing.",
            f"Picks & Shovels: Supply B2B tools, compliance workflows (OSS-RBA/Halal/SAK EMKM), or fulfillment to players entering '{sector}'.",
            f"Unbundling Gap: Strip out the single highest-margin job-to-be-done in '{sector}' into a fast fixed-price service.",
        ],
    }


def cmd_zero_rupiah_plan(args: argparse.Namespace) -> Dict[str, Any]:
    skill_or_asset = args.skill_or_network
    target_market = args.target_market
    target_monthly_income = float(args.target_monthly_profit_idr)

    tier_b2b_price = 2_500_000.0
    clients_needed = math.ceil(target_monthly_income / tier_b2b_price)
    po_unit_margin = 100_000.0
    po_units_needed = math.ceil(target_monthly_income / po_unit_margin)

    return {
        "status": "ok",
        "command": "zero-rupiah-plan",
        "advisory_role": ADVISORY_ROLE_STATEMENT,
        "core_leverage": skill_or_asset,
        "target_market": target_market,
        "target_monthly_profit_idr": target_monthly_income,
        "mathematical_principle": "Negative Cash Conversion Cycle (CCC < 0): Validate demand & collect 50-100% customer DP BEFORE incurring COGS.",
        "blueprints": [
            {
                "model": "1. B2B Productized Service / Automation Retainer (Customer-Funded)",
                "offer": f"Paket solusi terukur '{skill_or_asset}' untuk {target_market}.",
                "pricing_idr": tier_b2b_price,
                "upfront_dp_pct": 50,
                "sales_target": f"Target skenario: akuisisi {clients_needed} klien/bulan (@ Rp{tier_b2b_price:,.0f}) menuju target Rp{target_monthly_income:,.0f}/bulan.",
            },
            {
                "model": "2. Batch Pre-Order (PO) / Back-to-Back Offtaker (CCC < 0)",
                "offer": f"Kurasi paket khusus bagi {target_market} dengan sistem PO Batch berbatas kuota.",
                "margin_per_unit_idr": po_unit_margin,
                "sales_target": f"Target skenario: {po_units_needed} unit PO/bulan (@ estimasi margin bersih Rp{po_unit_margin:,.0f}/unit).",
            },
            {
                "model": "3. Idle-Capacity Revenue Share (Rainmaker Partnership)",
                "offer": f"Kerja sama bagi hasil (misal 30%:70%) memanfaatkan kapasitas jam sepi pemilik fasilitas di pasar {target_market}.",
                "capital_required_idr": 0,
            },
        ],
        "whatsapp_closing_script_id": (
            f"Selamat pagi/siang Kak/Pak/Bu [Nama], izin menyapa dengan sopan. Saya memperhatikan [Nama Usaha] di {target_market} "
            f"punya ruang menarik untuk mengoptimalkan [Manfaat Utama]. Kebetulan kami sedang membuka 3 slot pilot pendampingan "
            f"[{skill_or_asset}] yang ringkas dan terukur. Bila berkenan, boleh saya kirimkan 1 halaman ringkasan simulasinya di sini, Kak?"
        ),
    }


# ==============================================================================
# 3. ETERNAL-STUDENT RESEARCH LOOP, NEW-APP ONBOARDING & 49-SKILL SYNERGY
# ==============================================================================

def cmd_phd_learn(args: argparse.Namespace) -> Dict[str, Any]:
    state_dir = get_state_dir()
    session = load_session(state_dir)
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "topic": args.topic,
        "hypothesis_or_insight": args.insight,
        "category": args.category,
    }
    session.setdefault("learned_insights", []).append(entry)
    session.setdefault("history", []).append({"cmd": "phd-learn", "topic": args.topic, "ts": entry["timestamp"]})
    save_session(session, state_dir)

    ledger_md = state_dir / "phd_business_ledger" / "dissertation_notes.md"
    with ledger_md.open("a", encoding="utf-8") as f:
        f.write(f"\n## [{entry['timestamp'][:10]}] ({args.category}) {args.topic}\n- **Empirical Note / Hypothesis**: {args.insight}\n")

    return {
        "status": "ok",
        "command": "phd-learn",
        "message": "Empirical note recorded in Eternal-Student Business Ledger.",
        "ledger_file": str(ledger_md),
        "total_phd_insights": len(session["learned_insights"]),
        "entry": entry,
    }


def cmd_onboard_app(args: argparse.Namespace) -> Dict[str, Any]:
    """Inspect a newly connected CLI/business app, hash its capabilities, and track updates."""
    app_cmd = args.app
    state_dir = get_state_dir()
    snap_path = state_dir / "phd_business_ledger" / "app_capabilities_snapshot.json"
    snap: Dict[str, Any] = {"apps": {}}
    if snap_path.is_file():
        try:
            snap = json.loads(snap_path.read_text(encoding="utf-8"))
        except Exception:
            snap = {"apps": {}}

    bin_path = shutil.which(app_cmd)
    if not bin_path:
        return {
            "status": "ok",
            "command": "onboard-app",
            "app_command": app_cmd,
            "onboarding_state": "binary_not_on_path",
            "binary_path": None,
            "hint": f"Install `{app_cmd}` or its CLI-Anything harness (`cli-hub install {app_cmd}`), then re-run `bsage onboard-app --app {app_cmd}`.",
        }

    ver_out = ""
    help_out = ""
    for flag, holder in (("--version", "ver"), ("--help", "help")):
        try:
            p = subprocess.run([bin_path, flag], capture_output=True, text=True, timeout=6, check=False)
            txt = (p.stdout or p.stderr or "").strip()
            if holder == "ver":
                ver_out = txt.splitlines()[0][:200] if txt else "unknown"
            else:
                help_out = txt[:4000]
        except Exception:
            pass

    digest = hashlib.sha256(f"{ver_out}\n{help_out}".encode("utf-8", errors="replace")).hexdigest()[:16]
    prev = snap.get("apps", {}).get(app_cmd)
    if prev is None:
        state_label = "newly_onboarded_app"
    elif prev.get("capability_hash") != digest:
        state_label = "updated_capabilities_detected"
    else:
        state_label = "unchanged_up_to_date"

    snap.setdefault("apps", {})[app_cmd] = {
        "binary_path": bin_path,
        "version_line": ver_out or "detected",
        "capability_hash": digest,
        "checked_at": datetime.now(timezone.utc).isoformat(),
    }
    snap_path.write_text(json.dumps(snap, indent=2, ensure_ascii=False), encoding="utf-8")

    return {
        "status": "ok",
        "command": "onboard-app",
        "app_command": app_cmd,
        "onboarding_state": state_label,
        "binary_path": bin_path,
        "version_line": ver_out or "detected",
        "capability_hash": digest,
        "snapshot_file": str(snap_path),
    }


def cmd_synergy(args: argparse.Namespace) -> Dict[str, Any]:
    repo_root = resolve_repo_root(getattr(args, "repo", None))
    skills_root = Path(args.skills_root).expanduser() if getattr(args, "skills_root", None) else (
        (repo_root / "skills") if repo_root else None
    )
    if not skills_root or not skills_root.is_dir():
        return {"status": "error", "error": "Skills root directory not found."}

    skills_list: List[Dict[str, str]] = []
    for d in sorted(skills_root.iterdir(), key=lambda p: p.name.lower()):
        sk_md = d / "SKILL.md"
        if d.is_dir() and sk_md.is_file():
            desc = ""
            for line in sk_md.read_text(encoding="utf-8", errors="replace").splitlines()[:15]:
                if line.lower().startswith("description:"):
                    desc = line.split(":", 1)[1].strip()[:160]
                    break
            skills_list.append({"name": d.name, "description": desc})

    return {
        "status": "ok",
        "command": "synergy",
        "skills_root": str(skills_root),
        "total_collaborative_skills": len(skills_list),
        "skills": skills_list,
    }


# ==============================================================================
# 4. UNIVERSAL MULTI-AGENT INSTALLER, TERMINAL UPDATE CHECKER & SELF-UPDATER
# ==============================================================================

def _parse_github_owner_repo(repo_url: str) -> Tuple[str, str]:
    m = re.search(r"github\.com[:/]([^/]+)/([^/.]+?)(?:\.git)?$", repo_url.strip())
    if m:
        return m.group(1), m.group(2)
    return DEFAULT_GITHUB_OWNER, DEFAULT_GITHUB_REPO


def _detect_effective_repo_url(repo_root: Optional[Path], explicit_url: Optional[str] = None) -> str:
    if explicit_url:
        return explicit_url
    if repo_root and (repo_root / ".git").exists() and shutil.which("git"):
        try:
            p = subprocess.run(
                ["git", "-C", str(repo_root), "remote", "get-url", "origin"],
                capture_output=True,
                text=True,
                timeout=4,
                check=False,
            )
            if p.returncode == 0 and p.stdout.strip():
                return p.stdout.strip()
        except Exception:
            pass
    return f"https://github.com/{DEFAULT_GITHUB_OWNER}/{DEFAULT_GITHUB_REPO}.git"


def get_local_version_info(repo_root: Optional[Path]) -> Dict[str, Any]:
    ver = VERSION
    if repo_root and (repo_root / "VERSION").is_file():
        ver = (repo_root / "VERSION").read_text(encoding="utf-8").strip() or VERSION
    sha = None
    branch = DEFAULT_BRANCH
    if repo_root and (repo_root / ".git").exists() and shutil.which("git"):
        try:
            sp = subprocess.run(["git", "-C", str(repo_root), "rev-parse", "HEAD"], capture_output=True, text=True, timeout=4, check=False)
            if sp.returncode == 0:
                sha = sp.stdout.strip()
            bp = subprocess.run(["git", "-C", str(repo_root), "rev-parse", "--abbrev-ref", "HEAD"], capture_output=True, text=True, timeout=4, check=False)
            if bp.returncode == 0 and bp.stdout.strip():
                branch = bp.stdout.strip()
        except Exception:
            pass
    if not sha and repo_root and (repo_root / ".bsage_install_meta.json").is_file():
        try:
            sha = json.loads((repo_root / ".bsage_install_meta.json").read_text(encoding="utf-8")).get("commit_sha")
        except Exception:
            pass
    return {
        "repo_root": str(repo_root) if repo_root else None,
        "version": ver,
        "commit_sha": sha,
        "commit_short": sha[:7] if sha else "unpushed-local",
        "branch": branch,
    }


def _copy_or_link_skill(src_skill: Path, dst_skill: Path, prefer_link: bool = True, repo_root: Optional[Path] = None) -> str:
    try:
        if src_skill.resolve() == dst_skill.resolve():
            return "same_source_skipped"
    except OSError:
        pass

    if not dst_skill.parent.is_dir():
        try:
            os.lstat(str(dst_skill.parent))
            # Parent path exists as a file or dangling junction/symlink; do not overwrite user reparse points
            raise OSError(f"Target parent '{dst_skill.parent}' is a dangling junction/symlink or file.")
        except FileNotFoundError:
            dst_skill.parent.mkdir(parents=True, exist_ok=True)
    marker_name = ".bsage-managed"

    if dst_skill.is_symlink():
        dst_skill.unlink()
    elif dst_skill.exists():
        is_managed = (dst_skill / marker_name).is_file() or (dst_skill / ".hmfa-managed").is_file()
        is_junction_to_us = False
        try:
            resolved = dst_skill.resolve()
            if resolved == src_skill.resolve():
                return "same_source_skipped"
            if repo_root and repo_root.resolve() in resolved.parents:
                is_junction_to_us = True
            # Also detect Windows directory junction cleanly without destroying unmanaged data
            if platform.system() == "Windows" and resolved != dst_skill.absolute():
                is_junction_to_us = True
        except OSError:
            pass

        if is_junction_to_us and platform.system() == "Windows":
            try:
                os.rmdir(dst_skill)
            except OSError:
                shutil.rmtree(dst_skill)
        elif is_managed:
            shutil.rmtree(dst_skill)
        else:
            stamp = time.strftime("%Y%m%d-%H%M%S")
            backup = dst_skill.with_name(f"{dst_skill.name}.backup-{stamp}")
            shutil.move(str(dst_skill), str(backup))

    if prefer_link:
        try:
            dst_skill.symlink_to(src_skill, target_is_directory=True)
            return "symlinked"
        except OSError:
            if platform.system() == "Windows":
                try:
                    import _winapi  # type: ignore

                    _winapi.CreateJunction(str(src_skill), str(dst_skill))
                    if dst_skill.exists():
                        return "junction_linked"
                except Exception:
                    try:
                        proc = subprocess.run(
                            ["cmd", "/c", "mklink", "/J", str(dst_skill), str(src_skill)],
                            capture_output=True,
                            text=True,
                            timeout=5,
                            check=False,
                        )
                        if proc.returncode == 0 and dst_skill.exists():
                            return "junction_linked"
                    except Exception:
                        pass

    shutil.copytree(src_skill, dst_skill, ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store"))
    try:
        (dst_skill / marker_name).write_text("managed-by-business-sage\n", encoding="utf-8")
    except OSError:
        pass
    return "copied"


def _cli_bin_dir() -> Path:
    if platform.system() == "Windows":
        local_app = os.environ.get("LOCALAPPDATA") or str(Path.home() / "AppData" / "Local")
        return Path(local_app) / INSTALL_STATE_DIR_NAME / "bin"
    return Path.home() / ".local" / "bin"


def _ensure_windows_user_path(bin_dir: Path) -> bool:
    if platform.system() != "Windows":
        return False
    try:
        import winreg  # type: ignore

        target_str = str(bin_dir)
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment", 0, winreg.KEY_READ | winreg.KEY_WRITE) as key:
            try:
                current_path, reg_type = winreg.QueryValueEx(key, "Path")
            except FileNotFoundError:
                current_path, reg_type = "", winreg.REG_EXPAND_SZ
            parts = [p.strip() for p in str(current_path).split(";") if p.strip()]
            norm_parts = {os.path.normcase(os.path.expandvars(p).rstrip("\\/")) for p in parts}
            if os.path.normcase(target_str.rstrip("\\/")) not in norm_parts:
                winreg.SetValueEx(key, "Path", 0, reg_type, ";".join(parts + [target_str]))
                return True
    except Exception:
        return False
    return False


def install_terminal_launchers(repo_root: Path, hermes_roots: List[Path]) -> Dict[str, Any]:
    bin_dir = _cli_bin_dir()
    bin_dir.mkdir(parents=True, exist_ok=True)
    harness_dir = repo_root / "business-sage" / "agent-harness"

    cmd_dirs = [bin_dir] + [hr / "bin" for hr in hermes_roots if hr.is_dir()]
    written: List[str] = []

    for tbin in cmd_dirs:
        try:
            tbin.mkdir(parents=True, exist_ok=True)
            for name in ("bsage", "business-sage", "cli-anything-business-sage", "business-sage-update"):
                extra_arg = " update" if name == "business-sage-update" else ""
                if platform.system() == "Windows":
                    cmd_file = tbin / f"{name}.cmd"
                    cmd_file.write_text(
                        "@echo off\r\n"
                        "setlocal\r\n"
                        f'set "BSAGE_REPO={repo_root}"\r\n'
                        f'set "PYTHONPATH={harness_dir};%PYTHONPATH%"\r\n'
                        "where python >nul 2>nul\r\n"
                        "if %ERRORLEVEL% EQU 0 (\r\n"
                        f"    python -m cli_anything.business_sage{extra_arg} %*\r\n"
                        "    exit /b %ERRORLEVEL%\r\n"
                        ")\r\n"
                        "where py >nul 2>nul\r\n"
                        "if %ERRORLEVEL% EQU 0 (\r\n"
                        f"    py -3 -m cli_anything.business_sage{extra_arg} %*\r\n"
                        "    exit /b %ERRORLEVEL%\r\n"
                        ")\r\n"
                        f'powershell -NoProfile -ExecutionPolicy Bypass -File "{repo_root / "update.ps1"}" %*\r\n',
                        encoding="utf-8",
                    )
                    written.append(str(cmd_file))

                sh_file = tbin / name
                sh_file.write_text(
                    "#!/usr/bin/env sh\n"
                    f'export BSAGE_REPO="{repo_root.as_posix()}"\n'
                    f'export PYTHONPATH="{harness_dir.as_posix()}${{PYTHONPATH:+:$PYTHONPATH}}"\n'
                    "if command -v python3 >/dev/null 2>&1; then\n"
                    f'  exec python3 -m cli_anything.business_sage{extra_arg} "$@"\n'
                    "elif command -v python >/dev/null 2>&1; then\n"
                    f'  exec python -m cli_anything.business_sage{extra_arg} "$@"\n'
                    "else\n"
                    f'  exec sh "{(repo_root / "update.sh").as_posix()}" "$@"\n'
                    "fi\n",
                    encoding="utf-8",
                    newline="\n",
                )
                try:
                    sh_file.chmod(0o755)
                except OSError:
                    pass
        except OSError:
            continue

    path_added = _ensure_windows_user_path(bin_dir)
    return {
        "primary_bin_dir": str(bin_dir),
        "added_to_windows_user_path": path_added,
        "launchers_written_count": len(written),
        "commands_enabled": ["bsage", "business-sage", "cli-anything-business-sage", "business-sage-update"],
    }


def cmd_install(args: argparse.Namespace) -> Dict[str, Any]:
    repo_root = resolve_repo_root(getattr(args, "repo", None))
    if not repo_root or not (repo_root / "skills").is_dir():
        return {"status": "error", "error": "Repository root with `skills/` directory not found."}

    scope = getattr(args, "scope", "all")
    core_business = {"business-sage", "cli-anything-business-sage"}
    skill_dirs = sorted(
        [
            d
            for d in (repo_root / "skills").iterdir()
            if d.is_dir() and (d / "SKILL.md").is_file() and (scope == "all" or d.name in core_business)
        ],
        key=lambda p: p.name.lower(),
    )

    targets: List[Tuple[str, str, Path]] = []
    hermes_roots: List[Path] = []
    explicit_targets: List[str] = getattr(args, "target", None) or []

    if explicit_targets:
        for t in explicit_targets:
            targets.append(("explicit-target", f"Explicit Target ({t})", Path(t).expanduser()))
    else:
        hermes_list = discover_hermes_installations(deep_scan=True, explicit_home=getattr(args, "hermes_home", None))
        for h in hermes_list:
            h_root = Path(str(h["root"]))
            hermes_roots.append(h_root)
            targets.append(("hermes-root", f"Hermes Root ({h_root})", Path(str(h["skills_dir"]))))
            for prof in h["profiles"]:
                p_path = Path(str(prof["path"]))
                if (p_path / "skills").exists() or (p_path / "config.yaml").is_file():
                    targets.append(("hermes-profile", f"Hermes Bot Profile [{prof['name']}]", Path(str(prof["skills_dir"]))))

        if not getattr(args, "hermes_only", False):
            for ag in discover_other_agents():
                if ag["detected"]:
                    targets.append((str(ag["agent_id"]), str(ag["label"]), Path(str(ag["skills_dir"]))))

    dry_run = bool(getattr(args, "dry_run", False))
    prefer_link = not bool(getattr(args, "copy", False))
    summary: List[Dict[str, Any]] = []

    for kind, label, dest_dir in targets:
        if dry_run:
            summary.append({"kind": kind, "target": label, "skills_dir": str(dest_dir), "skills_count": len(skill_dirs), "mode": "dry_run"})
            continue
        modes: Dict[str, int] = {}
        errors: List[str] = []
        for sdir in skill_dirs:
            try:
                m = _copy_or_link_skill(sdir, dest_dir / sdir.name, prefer_link=prefer_link, repo_root=repo_root)
                modes[m] = modes.get(m, 0) + 1
            except Exception as exc:
                errors.append(f"{sdir.name}: {exc}")
        summary.append(
            {
                "kind": kind,
                "target": label,
                "skills_dir": str(dest_dir),
                "skills_synced": sum(modes.values()),
                "methods": modes,
                **({"warnings": errors} if errors else {}),
            }
        )

    launchers = {} if (dry_run or getattr(args, "no_launchers", False)) else install_terminal_launchers(repo_root, hermes_roots)
    return {
        "status": "ok",
        "command": "install",
        "scope": scope,
        "provider_model_lock_preserved": True,
        "skills_selected_count": len(skill_dirs),
        "targets": summary,
        "terminal_cli": launchers,
    }


def _http_get_text(url: str, timeout: int = 8) -> Optional[str]:
    req = urllib.request.Request(url, headers={"User-Agent": "business-sage-cli/2.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read().decode("utf-8", errors="replace").strip()
    except Exception:
        return None


def _http_get_json(url: str, timeout: int = 8) -> Optional[dict]:
    req = urllib.request.Request(
        url,
        headers={"Accept": "application/vnd.github+json", "User-Agent": "business-sage-cli/2.0"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode("utf-8", errors="replace"))
    except Exception:
        return None


def cmd_check(args: argparse.Namespace) -> Dict[str, Any]:
    repo_root = resolve_repo_root(getattr(args, "repo", None))
    repo_url = _detect_effective_repo_url(repo_root, getattr(args, "repo_url", None))
    owner, repo = _parse_github_owner_repo(repo_url)
    branch = getattr(args, "branch", DEFAULT_BRANCH)
    local = get_local_version_info(repo_root)

    remote_sha: Optional[str] = None
    remote_title: Optional[str] = None
    if shutil.which("git"):
        try:
            p = subprocess.run(
                ["git", "ls-remote", f"https://github.com/{owner}/{repo}.git", f"refs/heads/{branch}"],
                capture_output=True,
                text=True,
                timeout=8,
                check=False,
            )
            if p.returncode == 0 and p.stdout.strip():
                remote_sha = p.stdout.strip().split()[0]
        except Exception:
            pass

    cjson = _http_get_json(f"https://api.github.com/repos/{owner}/{repo}/commits/{branch}")
    if isinstance(cjson, dict) and cjson.get("sha"):
        remote_sha = remote_sha or str(cjson["sha"])
        cobj = cjson.get("commit", {})
        remote_title = (cobj.get("message") or "").splitlines()[0] if cobj else None

    remote_ver = _http_get_text(f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/VERSION")

    if not remote_sha and not remote_ver:
        return {
            "status": "pending_remote",
            "ok": False,
            "repository": f"{owner}/{repo}",
            "repo_url": repo_url,
            "local": local,
            "message": (
                f"Remote repository https://github.com/{owner}/{repo} is not yet published or reachable. "
                "Create the GitHub repo and run `./push_to_github.ps1` once, then `bsage check` will track live commits!"
            ),
        }

    local_sha = local.get("commit_sha")
    local_ahead = False
    if local_sha and remote_sha:
        if str(local_sha).lower() == str(remote_sha).lower():
            update_available = False
        else:
            update_available = True
            if repo_root and (repo_root / ".git").exists() and shutil.which("git"):
                try:
                    anc = subprocess.run(
                        ["git", "-C", str(repo_root), "merge-base", "--is-ancestor", str(remote_sha), str(local_sha)],
                        capture_output=True,
                        timeout=4,
                        check=False,
                    )
                    if anc.returncode == 0:
                        update_available = False
                        local_ahead = True
                except Exception:
                    pass
    else:
        update_available = bool(remote_ver and str(local.get("version")) != str(remote_ver))

    return {
        "status": "ok",
        "ok": True,
        "repository": f"{owner}/{repo}",
        "branch": branch,
        "update_available": update_available,
        "local_ahead_of_remote": local_ahead,
        "local": local,
        "remote": {
            "version": remote_ver or "unknown",
            "commit_sha": remote_sha,
            "commit_short": remote_sha[:7] if remote_sha else "unknown",
            "latest_commit_title": remote_title,
        },
        "command_to_update": "bsage update",
    }


def cmd_update(args: argparse.Namespace) -> Dict[str, Any]:
    repo_root = resolve_repo_root(getattr(args, "repo", None))
    check_res = cmd_check(args)
    if not check_res.get("ok"):
        return check_res

    scope = getattr(args, "scope", "business")
    force = bool(getattr(args, "force", False))
    branch = getattr(args, "branch", DEFAULT_BRANCH)
    owner, repo = str(check_res["repository"]).split("/", 1)

    if not check_res.get("update_available") and not force and repo_root:
        inst_ns = argparse.Namespace(
            repo=str(repo_root),
            scope=scope,
            target=[],
            hermes_home=None,
            hermes_only=getattr(args, "hermes_only", False),
            copy=False,
            dry_run=False,
            no_launchers=False,
        )
        sync_res = cmd_install(inst_ns)
        return {
            "status": "ok",
            "ok": True,
            "updated": False,
            "message": "Already at latest version! Verified agent skill links.",
            "check": check_res,
            "sync": sync_res,
        }

    target_root = repo_root or (get_state_dir() / "github_sync_cache")
    target_root.mkdir(parents=True, exist_ok=True)
    method = "none"

    if (target_root / ".git").exists() and shutil.which("git"):
        fp = subprocess.run(["git", "-C", str(target_root), "fetch", "origin", branch], capture_output=True, text=True, timeout=30, check=False)
        pp = subprocess.run(["git", "-C", str(target_root), "pull", "--ff-only", "origin", branch], capture_output=True, text=True, timeout=30, check=False)
        if fp.returncode == 0 and pp.returncode == 0:
            method = "git_pull_ff_only"
        else:
            return {
                "status": "error",
                "ok": False,
                "error": "Git fast-forward pull paused safely due to local uncommitted edits.",
                "git_output": (pp.stderr or pp.stdout).strip(),
            }
    else:
        zip_url = f"https://codeload.github.com/{owner}/{repo}/zip/refs/heads/{branch}"
        with tempfile.TemporaryDirectory() as tmpd:
            zpath = Path(tmpd) / "repo.zip"
            req = urllib.request.Request(zip_url, headers={"User-Agent": "business-sage-cli/2.0"})
            with urllib.request.urlopen(req, timeout=45) as r:
                zpath.write_bytes(r.read())
            ex_dir = Path(tmpd) / "extracted"
            with zipfile.ZipFile(zpath, "r") as zf:
                zf.extractall(ex_dir)
            subs = [d for d in ex_dir.iterdir() if d.is_dir()]
            if not subs:
                return {"status": "error", "ok": False, "error": "Downloaded archive was empty."}
            for item in subs[0].iterdir():
                if item.name in {"phd_business_ledger", ".git"}:
                    continue
                dst = target_root / item.name
                if dst.is_dir():
                    shutil.rmtree(dst)
                elif dst.exists():
                    dst.unlink()
                if item.is_dir():
                    shutil.copytree(item, dst)
                else:
                    shutil.copy2(item, dst)
        rem = check_res.get("remote", {})
        if isinstance(rem, dict):
            (target_root / ".bsage_install_meta.json").write_text(
                json.dumps({"commit_sha": rem.get("commit_sha")}, indent=2),
                encoding="utf-8",
            )
        method = "https_zip_archive"

    inst_ns = argparse.Namespace(
        repo=str(target_root),
        scope=scope,
        target=[],
        hermes_home=None,
        hermes_only=getattr(args, "hermes_only", False),
        copy=False,
        dry_run=False,
        no_launchers=False,
    )
    sync_res = cmd_install(inst_ns)
    return {
        "status": "ok",
        "ok": True,
        "updated": True,
        "update_method": method,
        "now_installed": get_local_version_info(target_root),
        "sync": sync_res,
    }


def export_chatgpt_bundle(repo_root: Path, out_dir: Optional[Path] = None) -> Dict[str, Any]:
    dest = out_dir or (repo_root / "exports" / "chatgpt")
    dest.mkdir(parents=True, exist_ok=True)
    inst_src = repo_root / "adapters" / "chatgpt" / "CHATGPT_CUSTOM_INSTRUCTIONS.md"
    inst_dst = dest / "01_PASTE_INTO_CHATGPT_INSTRUCTIONS.md"
    if inst_src.is_file():
        shutil.copy2(inst_src, inst_dst)

    parts: List[str] = [
        "# Business Sage — Consolidated Knowledge Base (S1-S2 Business, Finance & Indonesian UMKM/Tax Co-Pilot)\n",
        f"> Role: {ADVISORY_ROLE_STATEMENT}\n\n",
    ]
    sources = [
        repo_root / "skills" / "business-sage" / "SKILL.md",
        repo_root / "skills" / "business-sage" / "references" / "s1-s2-mba-global-and-financial-literacy.md",
        repo_root / "skills" / "business-sage" / "references" / "indonesia-economic-tax-legal-system.md",
        repo_root / "skills" / "business-sage" / "references" / "trend-prediction-profit-gaps-and-zero-rupiah.md",
        repo_root / "skills" / "business-sage" / "references" / "customer-psychology-sales-and-phd-loop.md",
        repo_root / "skills" / "business-sage" / "references" / "cross-skill-synergy-and-new-app-onboarding.md",
        repo_root / "skills" / "cli-anything-business-sage" / "SKILL.md",
    ]
    packed: List[str] = []
    for fp in sources:
        if fp.is_file():
            rel = fp.relative_to(repo_root).as_posix()
            parts.append(f"\n\n---\n## Source: `{rel}`\n\n")
            parts.append(fp.read_text(encoding="utf-8", errors="replace"))
            packed.append(rel)

    kb_dst = dest / "02_UPLOAD_AS_CHATGPT_KNOWLEDGE_BASE.md"
    kb_dst.write_text("".join(parts), encoding="utf-8")
    return {
        "status": "ok",
        "command": "export-chatgpt",
        "output_dir": str(dest),
        "instructions_file": str(inst_dst),
        "knowledge_base_file": str(kb_dst),
        "sources_packed": packed,
    }


def cmd_status(args: argparse.Namespace) -> Dict[str, Any]:
    repo_root = resolve_repo_root(getattr(args, "repo", None))
    session = load_session()
    hermes_list = discover_hermes_installations(deep_scan=True)
    other_agents = discover_other_agents()
    skill_dirs = discover_agent_skill_dirs(deep_scan=True)
    return {
        "status": "ok",
        "tool": "cli-anything-business-sage",
        "version": VERSION,
        "advisor_role": ADVISORY_ROLE_STATEMENT,
        "phd_status": session.get("phd_level"),
        "local_repo": get_local_version_info(repo_root),
        "state_dir": str(get_state_dir()),
        "hermes_installations": hermes_list,
        "other_agents": other_agents,
        "detected_agent_skill_dirs": skill_dirs,
        "learned_insights_count": len(session.get("learned_insights", [])),
        "history_count": len(session.get("history", [])),
    }


def cmd_discover(args: argparse.Namespace) -> Dict[str, Any]:
    return {
        "status": "ok",
        "command": "discover",
        "hermes": discover_hermes_installations(deep_scan=True, explicit_home=getattr(args, "hermes_home", None)),
        "other_agents": discover_other_agents(),
    }


def cmd_export_chatgpt(args: argparse.Namespace) -> Dict[str, Any]:
    repo_root = resolve_repo_root(getattr(args, "repo", None))
    if not repo_root:
        return {"status": "error", "error": "Repository root not found."}
    out = Path(args.out).expanduser() if getattr(args, "out", None) else None
    return export_chatgpt_bundle(repo_root, out)


# ==============================================================================
# 5. PARSER, HUMAN-READABLE TERMINAL FORMATTER & STATEFUL REPL
# ==============================================================================

class BusinessSageREPL(cmd.Cmd):
    intro = (
        "====================================================================\n"
        " BUSINESS SAGE REPL — Strategy. Finance. Growth. (v2.0.0)\n"
        " (CLI-Anything Compatible | Zero MCP Token Overhead | Co-Pilot)\n"
        " Type 'status', 'check', 'update', 'synergy', 'help', or 'exit'.\n"
        "===================================================================="
    )
    prompt = "bsage> "

    def default(self, line: str) -> None:
        if line.strip() in {"EOF", "exit", "quit"}:
            return
        try:
            main(shlex.split(line))
        except SystemExit:
            pass

    def do_exit(self, _arg: str) -> bool:
        return True

    def do_quit(self, _arg: str) -> bool:
        return True

    def do_EOF(self, _arg: str) -> bool:
        print()
        return True


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="bsage",
        description=(
            "Business Sage CLI-Anything Harness: S1-S2 Business & Financial Scenario Co-Pilot "
            "(respecting business students & practitioners), Eternal-Student Loop & Multi-Agent Auto-Updater."
        ),
    )
    parser.add_argument("--json", action="store_true", help="Emit deterministic machine-readable JSON output.")
    parser.add_argument("--repo", default=None, help="Explicit Business Sage repository root.")
    sub = parser.add_subparsers(dest="subcommand")

    for alias in ("status", "doctor"):
        p_st = sub.add_parser(alias, help="Inspect Business Sage status, Hermes (#1) roots & multi-agent paths.")
        p_st.add_argument("--json", action="store_true", dest="sub_json")
        p_st.set_defaults(func=cmd_status)

    p_disc = sub.add_parser("discover", help="Scan all drives & env for Hermes (#1) and supported AI agents.")
    p_disc.add_argument("--json", action="store_true", dest="sub_json")
    p_disc.add_argument("--hermes-home", default=None)
    p_disc.set_defaults(func=cmd_discover)

    p_inst = sub.add_parser("install", help="Auto-discover Hermes + multi-agent folders and install Business Sage skills.")
    p_inst.add_argument("--json", action="store_true", dest="sub_json")
    p_inst.add_argument("--scope", default="business", choices=["business", "all"], help="'business' (2 core skills) or 'all' (49 skills).")
    p_inst.add_argument("--target", action="append", default=[], help="Explicit target skills directory override.")
    p_inst.add_argument("--hermes-home", default=None)
    p_inst.add_argument("--hermes-only", action="store_true")
    p_inst.add_argument("--copy", action="store_true", help="Copy files instead of junctions/symlinks.")
    p_inst.add_argument("--dry-run", action="store_true")
    p_inst.add_argument("--no-launchers", action="store_true")
    p_inst.set_defaults(func=cmd_install)

    p_chk = sub.add_parser("check", help="Check GitHub for Business Sage updates directly from terminal.")
    p_chk.add_argument("--json", action="store_true", dest="sub_json")
    p_chk.add_argument("--repo-url", default=None)
    p_chk.add_argument("--branch", default=DEFAULT_BRANCH)
    p_chk.set_defaults(func=cmd_check)

    p_upd = sub.add_parser("update", help="Pull latest updates from GitHub & sync into Hermes + detected agents.")
    p_upd.add_argument("--json", action="store_true", dest="sub_json")
    p_upd.add_argument("--repo-url", default=None)
    p_upd.add_argument("--branch", default=DEFAULT_BRANCH)
    p_upd.add_argument("--scope", default="business", choices=["business", "all"])
    p_upd.add_argument("--hermes-only", action="store_true")
    p_upd.add_argument("--force", action="store_true")
    p_upd.set_defaults(func=cmd_update)

    p_lit = sub.add_parser("literacy-audit", help="Run 16-Unit Financial Literacy & 50/30/20 runway audit.")
    p_lit.add_argument("--json", action="store_true", dest="sub_json")
    p_lit.add_argument("--monthly-after-tax-income", required=True, type=float)
    p_lit.add_argument("--monthly-needs", required=True, type=float)
    p_lit.add_argument("--monthly-wants", required=True, type=float)
    p_lit.add_argument("--monthly-savings", required=True, type=float)
    p_lit.add_argument("--liquid-emergency-cash", required=True, type=float)
    p_lit.add_argument("--high-apr-debt", default=0.0, type=float)
    p_lit.set_defaults(func=cmd_literacy_audit)

    p_ue = sub.add_parser("unit-economics", help="Compute Contribution Margin, BEP, Gross-Margin LTV, CAC & Payback.")
    p_ue.add_argument("--json", action="store_true", dest="sub_json")
    p_ue.add_argument("--price", required=True, type=float)
    p_ue.add_argument("--variable-cost", required=True, type=float)
    p_ue.add_argument("--monthly-fixed-cost", required=True, type=float)
    p_ue.add_argument("--cac", required=True, type=float)
    p_ue.add_argument("--monthly-churn-rate", default=0.05, type=float)
    p_ue.set_defaults(func=cmd_unit_economics)

    p_dcf = sub.add_parser("valuation-dcf", help="Compute 5-year FCFF & Terminal Value Intrinsic DCF Valuation.")
    p_dcf.add_argument("--json", action="store_true", dest="sub_json")
    p_dcf.add_argument("--initial-fcff", required=True, type=float)
    p_dcf.add_argument("--growth-rate-5yr", required=True, type=float)
    p_dcf.add_argument("--terminal-growth-rate", default=0.03, type=float)
    p_dcf.add_argument("--wacc", required=True, type=float)
    p_dcf.add_argument("--cash", default=0.0, type=float)
    p_dcf.add_argument("--debt", default=0.0, type=float)
    p_dcf.set_defaults(func=cmd_valuation_dcf)

    p_id = sub.add_parser("indonesia-tax-legal", help="Model Indonesian UMKM tier (PP 7/2021) & Tax Scenarios (PP 20/2026 vs Pasal 31E).")
    p_id.add_argument("--json", action="store_true", dest="sub_json")
    p_id.add_argument("--annual-turnover-idr", required=True, type=float)
    p_id.add_argument("--annual-net-profit-idr", required=True, type=float)
    p_id.add_argument("--entity-type", default="pt_perorangan", choices=["wp_op", "pt_perorangan", "cv", "pt_biasa", "koperasi"])
    p_id.set_defaults(func=cmd_indonesia_tax_legal)

    p_tr = sub.add_parser("predict-trend", help="Forecast trend adoption window via Bass Diffusion S-Curve & Geo-Lag Arbitrage.")
    p_tr.add_argument("--json", action="store_true", dest="sub_json")
    p_tr.add_argument("--sector", required=True)
    p_tr.add_argument("--innovation-coeff-p", default=0.02, type=float)
    p_tr.add_argument("--imitation-coeff-q", default=0.38, type=float)
    p_tr.add_argument("--current-adoption-pct", default=8.0, type=float)
    p_tr.set_defaults(func=cmd_predict_trend)

    p_zr = sub.add_parser("zero-rupiah-plan", help="Generate Modal Rp0 Negative-CCC blueprints & WhatsApp WARMTH script.")
    p_zr.add_argument("--json", action="store_true", dest="sub_json")
    p_zr.add_argument("--skill-or-network", required=True)
    p_zr.add_argument("--target-market", required=True)
    p_zr.add_argument("--target-monthly-profit-idr", default=10000000.0, type=float)
    p_zr.set_defaults(func=cmd_zero_rupiah_plan)

    p_phd = sub.add_parser("phd-learn", help="Record an empirical note or hypothesis in the Eternal-Student Ledger.")
    p_phd.add_argument("--json", action="store_true", dest="sub_json")
    p_phd.add_argument("--topic", required=True)
    p_phd.add_argument("--insight", required=True)
    p_phd.add_argument("--category", default="Business-Method")
    p_phd.set_defaults(func=cmd_phd_learn)

    p_app = sub.add_parser("onboard-app", help="Eternal-Student capability introspection for newly connected CLI/business apps.")
    p_app.add_argument("--json", action="store_true", dest="sub_json")
    p_app.add_argument("--app", required=True)
    p_app.set_defaults(func=cmd_onboard_app)

    p_syn = sub.add_parser("synergy", help="List all collaborative skills connected to Business Sage.")
    p_syn.add_argument("--json", action="store_true", dest="sub_json")
    p_syn.add_argument("--skills-root", default=None)
    p_syn.set_defaults(func=cmd_synergy)

    p_gpt = sub.add_parser("export-chatgpt", help="Export ready-to-upload ChatGPT Custom GPT / Project bundle.")
    p_gpt.add_argument("--json", action="store_true", dest="sub_json")
    p_gpt.add_argument("--out", default=None)
    p_gpt.set_defaults(func=cmd_export_chatgpt)

    return parser


def _print_human_or_json(cmd_name: str, res: Dict[str, Any], as_json: bool) -> None:
    if as_json:
        sys.stdout.write(json.dumps(res, indent=2, ensure_ascii=False) + "\n")
        return

    if cmd_name == "check":
        if not res.get("ok"):
            print("============================================================")
            print(" BUSINESS SAGE — TERMINAL UPDATE CHECK")
            print("============================================================")
            print(f" Local Version : v{res['local']['version']} ({res['local']['commit_short']})")
            print(f" Remote Status : {res.get('message')}")
            print("============================================================")
            return
        loc = res["local"]
        rem = res["remote"]
        rem_ver = f"v{rem['version']}" if rem.get("version") and rem["version"] != "unknown" else "pre-v2.0"
        st_txt = "UPDATE AVAILABLE! Run: bsage update" if res["update_available"] else "UP TO DATE (Latest)"
        print("============================================================")
        print(" BUSINESS SAGE — TERMINAL UPDATE CHECK")
        print("============================================================")
        print(f" Local Version  : v{loc['version']} ({loc['commit_short']})")
        print(f" Remote Version : {rem_ver} ({rem['commit_short']})")
        print(f" Latest Commit  : {rem.get('latest_commit_title') or 'N/A'}")
        print(f" Status         : {st_txt}")
        print("============================================================")
        return

    if cmd_name in ("status", "doctor"):
        loc = res["local_repo"]
        print("============================================================")
        print(" BUSINESS SAGE DOCTOR — HERMES (#1) & MULTI-AGENT STATUS")
        print("============================================================")
        print(f" Role           : {res['advisor_role']}")
        print(f" Repo Root      : {loc.get('repo_root')}")
        print(f" Version        : v{loc.get('version')} ({loc.get('commit_short')})")
        print(f" Hermes (#1)    : {len(res['hermes_installations'])} installation(s) auto-detected")
        for h in res["hermes_installations"]:
            pnames = ", ".join(p["name"] for p in h["profiles"]) or "default only"
            print(f"   * {h['root']} [via {h['discovery_source']}] (profiles: {pnames})")
        det_others = [a for a in res["other_agents"] if a["detected"]]
        print(f" Other Agents   : {len(det_others)} detected")
        for a in det_others:
            print(f"   * {a['label']} -> {a['skills_dir']}")
        print("============================================================")
        return

    if cmd_name == "install":
        print("============================================================")
        print(" BUSINESS SAGE — UNIVERSAL HERMES (#1) & MULTI-AGENT INSTALLER")
        print("============================================================")
        print(f" Scope               : {res.get('scope')} ({res.get('skills_selected_count')} skill(s))")
        print(" Provider/Model Lock : 100% UNTOUCHED")
        print("------------------------------------------------------------")
        for t in res.get("targets", []):
            if t.get("warnings") and t.get("skills_synced", 0) == 0:
                print(f" [SKIP] {t['target']} -> {t['skills_dir']} (dangling link preserved safely)")
            else:
                print(f" [OK] {t['target']} -> {t['skills_dir']}")
        cli_info = res.get("terminal_cli") or {}
        if cli_info:
            print("------------------------------------------------------------")
            print(" Terminal Commands   : bsage check | bsage update | bsage status")
            print(f" Launcher Bin Dir    : {cli_info.get('primary_bin_dir')}")
        return

    sys.stdout.write(json.dumps(res, indent=2, ensure_ascii=False) + "\n")


def main(argv: Optional[List[str]] = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass

    parser = build_parser()
    args = parser.parse_args(argv)
    as_json = bool(getattr(args, "json", False) or getattr(args, "sub_json", False))

    if not args.subcommand:
        if as_json:
            sys.stdout.write(json.dumps(cmd_status(args), indent=2, ensure_ascii=False) + "\n")
            return 0
        BusinessSageREPL().cmdloop()
        return 0

    res = args.func(args)
    _print_human_or_json(args.subcommand, res, as_json)
    return 0 if res.get("status") in {"ok", "pending_remote"} else 1


def main_update_shortcut() -> int:
    return main(["update"] + sys.argv[1:])


if __name__ == "__main__":
    raise SystemExit(main())
