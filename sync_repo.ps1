# Sincronización universal de tu repositorio local con GitHub
Write-Host "
🚀 Iniciando sincronización del repositorio..." -ForegroundColor Cyan

# Muestra la ruta actual y el estado antes de hacer nada
Write-Host "
📂 Carpeta actual: C:\Users\usuario\GeneForge" -ForegroundColor Yellow
git status

# Añade TODOS los archivos nuevos y cambios
git add .

# Comprueba si hay cambios para commitear
 = git status --porcelain
if () {
    # Haz commit
     = "Sync: actualización automática de todo el pipeline, parser, razonador y ejemplos"
    git commit -m ""
    Write-Host "
✅ Commit realizado: " -ForegroundColor Green
}
else {
    Write-Host "
ℹ️ No hay cambios nuevos para commitear." -ForegroundColor Yellow
}

# Sube a la rama principal (main)
git push origin main
Write-Host "
🟢 Sincronización con GitHub completada." -ForegroundColor Green
