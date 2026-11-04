# Script opcional para Windows local.
# Requer que Python já esteja instalado e acessível no PATH.
$ErrorActionPreference = "Stop"

$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonCmd) {
    Write-Host "Python não foi encontrado. Este script não instala Python." -ForegroundColor Yellow
    Write-Host "Use GitHub Codespaces ou solicite a instalação à equipe de TI."
    exit 1
}

python -m venv .venv
if ($LASTEXITCODE -ne 0) { throw "Não foi possível criar o ambiente virtual." }

& .\.venv\Scripts\python.exe -m pip install --upgrade pip
& .\.venv\Scripts\python.exe -m pip install -r requirements.txt

Write-Host ""
Write-Host "Ambiente preparado. Para executar:" -ForegroundColor Green
Write-Host ".\.venv\Scripts\python.exe app.py"
