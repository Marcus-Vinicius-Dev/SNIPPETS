# Desativar a exibição de comandos
$ErrorActionPreference = "SilentlyContinue"

Write-Output "`nBem vindo ao Udjat`n"

# Fabricante do PC e placa-mãe
Write-Output "Fabricante do pc e placa-mae"
Get-WmiObject Win32_BaseBoard | Format-Table Manufacturer, Product, Version, SerialNumber -AutoSize
Write-Output "`n____________________________________________________________________________________________`n"


# Modelo do PC
Write-Output "Modelo do pc"
Get-WmiObject Win32_ComputerSystem | Select-Object -ExpandProperty Model
Write-Output "`n____________________________________________________________________________________________`n"


# BIOS
Write-Output "BIOS"
Get-WmiObject Win32_BIOS | Select-Object -ExpandProperty SMBIOSBIOSVersion
Write-Output "`n____________________________________________________________________________________________`n"


# Processador
Write-Output "Processador"
Get-WmiObject Win32_Processor | Format-Table Name, MaxClockSpeed, NumberOfCores -AutoSize
Write-Output "`n____________________________________________________________________________________________`n"


# Quantidade de discos
Write-Output "Quantidade de discos"
Get-PSDrive -PSProvider FileSystem | Select-Object -ExpandProperty Name
Write-Output "`n____________________________________________________________________________________________`n"


# Espaço livre dos discos
Write-Output "Espaco livre dos discos"
Get-PSDrive -PSProvider FileSystem | Format-Table Name, @{Label="Size (GB)"; Expression={[math]::round($_.Used / 1GB, 2)}}, @{Label="FreeSpace (GB)"; Expression={[math]::round($_.Free / 1GB, 2)}} -AutoSize
Write-Output "`n____________________________________________________________________________________________`n"


# Informações dos discos
Write-Output "Informacoes dos discos"
Get-WmiObject Win32_DiskDrive | Format-Table DeviceID, Caption, @{Label="Size (GB)"; Expression={[math]::round($_.Size / 1GB, 2)}}, MediaType -AutoSize
Write-Output "`n____________________________________________________________________________________________`n"


# Partições
Write-Output "Particoes"
Get-WmiObject Win32_DiskPartition | Select-Object -ExpandProperty DeviceID
Write-Output "`n____________________________________________________________________________________________`n"


# Slots de memória
Write-Output "Slots de memoria"
Get-WmiObject Win32_PhysicalMemory | Select-Object -ExpandProperty DeviceLocator
Write-Output "`n____________________________________________________________________________________________`n"


# Módulos de memória
Write-Output "Modulos de memorias"
Get-WmiObject Win32_PhysicalMemory | Format-Table Capacity, Speed, FormFactor, MemoryType -AutoSize
Write-Output "`n____________________________________________________________________________________________`n"


# Placa de vídeo
Write-Output "Placa de video"
Get-WmiObject Win32_VideoController | Format-Table Caption, @{Label="Adapter RAM (MB)"; Expression={[math]::round($_.AdapterRAM / 1MB, 2)}} -AutoSize
Write-Output "`n____________________________________________________________________________________________`n"


# Dispositivos de som
Write-Output "Dispositivos de Som"
Get-WmiObject Win32_SoundDevice | Format-Table Caption, DeviceID -AutoSize
Write-Output "`n____________________________________________________________________________________________`n"


# Informações da bateria
Write-Output "Informacoes da Bateria"
Get-WmiObject Win32_Battery | Format-Table Caption, Description, EstimatedChargeRemaining -AutoSize
Write-Output "`n____________________________________________________________________________________________`n"


# Impressoras instaladas
Write-Output "Impressoras Instaladas"
Get-WmiObject Win32_Printer | Format-Table Name, PortName -AutoSize
Write-Output "`n____________________________________________________________________________________________`n"


# Dispositivos USB conectados
Write-Output "Dispositivos USB Conectados"
Get-WmiObject Win32_PnPSignedDriver | Format-Table DeviceName, DriverVersion -AutoSize
Write-Output "`n____________________________________________________________________________________________`n"


# Adaptadores de rede
Write-Output "Adaptadores de Rede"
Get-WmiObject Win32_NetworkAdapter | Where-Object { $_.MACAddress -ne $null } | Format-Table Name, MACAddress -AutoSize
Write-Output "`n____________________________________________________________________________________________`n"


# Adaptadores Bluetooth
Write-Output "Adaptadores Bluetooth"
Get-WmiObject Win32_PnPEntity | Where-Object { $_.PNPClass -eq "Bluetooth" } | Format-Table Caption, Status -AutoSize
Write-Output "`n____________________________________________________________________________________________`n"


# Sistema operacional
Write-Output "Sistema operacional"
Get-WmiObject Win32_OperatingSystem | Format-Table Caption, Version, OSArchitecture, SerialNumber, InstallDate, LastBootUpTime, OSLanguage, Organization -AutoSize
Write-Output "`n____________________________________________________________________________________________`n"


# Contas de usuário
Write-Output "Contas de usuarios"
Get-LocalUser | Format-Table Name, Enabled -AutoSize
Write-Output "`n____________________________________________________________________________________________`n"


# Informações de IP
Write-Output "Informacoes do ip"
ipconfig
Write-Output "`n____________________________________________________________________________________________`n"


# Configuração de rede
Write-Output "Configuracao de Rede"
ipconfig /all
Write-Output "`n____________________________________________________________________________________________`n"


# Programas instalados
Write-Output "Programas Instalados"
Write-Output "Aguarde enquanto os programas instalados estao sendo listados...isso pode levar alguns minutos..."
Get-WmiObject Win32_Product | Format-Table Name, Version -AutoSize
Write-Output "`n____________________________________________________________________________________________`n"


# Fim
Write-Output "Fim."
Read-Host "Pressione Enter para sair..."
