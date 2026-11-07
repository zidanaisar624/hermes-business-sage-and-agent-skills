from pathlib import Path
from setuptools import find_namespace_packages, setup

ROOT = Path(__file__).resolve().parent
VERSION_FILE = ROOT.parent.parent / "VERSION"
VERSION = VERSION_FILE.read_text(encoding="utf-8").strip() if VERSION_FILE.is_file() else "2.0.0"

setup(
    name="cli-anything-business-sage",
    version=VERSION,
    description=(
        "CLI-Anything compatible zero-MCP-token harness for Business Sage: Internet-researched "
        "S1-S2 Business & Financial Advisor (respecting business students & practitioners), "
        "Indonesian UMKM/Tax Scenarios, Eternal-Student Research Loop, Multi-Agent Auto-Discovery & Terminal Updater."
    ),
    long_description=(ROOT / "BUSINESS_SAGE.md").read_text(encoding="utf-8")
    if (ROOT / "BUSINESS_SAGE.md").is_file()
    else "",
    long_description_content_type="text/markdown",
    author="Muhammad Zidan Aisar (MuZA) & Google Gemini",
    url="https://github.com/zidanaisar624/hermes-business-sage-and-agent-skills",
    license="MIT",
    python_requires=">=3.8",
    packages=find_namespace_packages(include=["cli_anything.*"]),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "bsage=cli_anything.business_sage.cli_anything_business_sage:main",
            "business-sage=cli_anything.business_sage.cli_anything_business_sage:main",
            "cli-anything-business-sage=cli_anything.business_sage.cli_anything_business_sage:main",
            "business-sage-update=cli_anything.business_sage.cli_anything_business_sage:main_update_shortcut",
        ],
    },
)
