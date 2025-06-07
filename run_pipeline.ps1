# run_pipeline.ps1
Write-Host '1) Limpiando BOM del archivo...' -ForegroundColor Cyan
Get-Content test_structured.gfl | Out-File -Encoding ascii test_structured_noBOM.gfl

Write-Host '2) Parseando GFL estructurado...' -ForegroundColor Cyan
python parse_gfl_struct.py

Write-Host '3) Ejecutando razonador avanzado...' -ForegroundColor Cyan
python razonador_avanzado.py
