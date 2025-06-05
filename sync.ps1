# sync.ps1
Set-Location "$env:USERPROFILE\GeneForge"

# Añadir todos los cambios
git add .

# Crear mensaje de commit con fecha y hora actuales
$timestamp = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
$commitMessage = "🔄 Sync update - $timestamp"
git commit -m "$commitMessage" 2>$null

# Empujar al repositorio remoto
git push origin main
