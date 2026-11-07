# Panduan Cepat: Instalasi Otomatis, Terminal Auto-Update (`bsage`) & Multi-Agent

> **Etika & Penghormatan untuk Anak Bisnis**: `business-sage` adalah *Strategic & Financial Co-Pilot* berbasis riset literatur publik S1–S2 bisnis, bukan pengganti mahasiswa/lulusan bisnis, pengusaha, Akuntan Publik, maupun Konsultan Pajak/Hukum resmi. Skrip di bawah ini **100% aman dan tidak pernah mengubah `config.yaml`, `provider`, `model`, atau `SOUL.md` Hermes Anda**.

## 1. Instalasi di Windows (`PowerShell` atau `CMD`)

```powershell
# Opsi Otomatis (Mencari semua instalasi Hermes + profil bot + OpenClaw/Claude/Codex di semua drive):
.\install_business_sage.ps1                # Memasang 2 skill inti Business Sage + CLI `bsage`
.\install.ps1 -Scope all                   # Memasang seluruh 49 skills kolaboratif + CLI `bsage`

# Opsi Target Eksplisit (Jika hanya ingin ke 1 folder tertentu, dengan preview -WhatIf):
.\install_business_sage.ps1 -TargetSkillsDir "$HOME\.hermes\skills" -Scope business -WhatIf
.\install_business_sage.ps1 -TargetSkillsDir "$HOME\.hermes\skills" -Scope business
```

## 2. Instalasi di Linux / macOS / WSL

```bash
bash ./install_business_sage.sh            # Auto-discovery multi-agent (2 skill inti)
bash ./install.sh                          # Auto-discovery multi-agent (seluruh 49 skills)
```

## 3. Cek & Update Langsung dari Terminal Kapan Saja

Dari folder mana pun (bahkan `C:\`), cukup ketik di **PowerShell** atau **CMD**:

```powershell
bsage check      # Cek apakah ada versi/commit baru di GitHub
bsage update     # Download update terbaru & sinkronkan ke Hermes + semua agent
bsage status     # Tampilkan status Hermes, agent lain, & Eternal-Student Ledger
```

## 4. Pakai di ChatGPT & Claude Web/Desktop

- **ChatGPT (Custom GPT / Project)**: Buka [`exports/chatgpt/`](./exports/chatgpt/), tempel isi `01_PASTE_INTO_CHATGPT_INSTRUCTIONS.md` ke kolom *Instructions*, dan unggah `02_UPLOAD_AS_CHATGPT_KNOWLEDGE_BASE.md` ke *Knowledge*.
- **Claude Projects / Claude Code**: Lihat [`adapters/claude/CLAUDE_PROJECT_GUIDE.md`](./adapters/claude/CLAUDE_PROJECT_GUIDE.md).
