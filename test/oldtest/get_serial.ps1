param(
    [string]$file_name
)

$FOLDER_PATH = "C:\Users\2003s\OneDrive\Desktop\Internship\csv_fold"
function difference {
    param(
        [string]$ds1,
        [string]$ds2
    )
    $d1 = [datetime]$ds1
    $d2 = [datetime]$ds2
    return (($d1.Year - $d2.Year) * 12) + $d1.Month - $d2.Month
}
function Get-SortedFilesByMonth {
    param (
        [int]$Month,
        [int]$Year
    )
    $FolderPath = $FOLDER_PATH
    # Retrieve and sort files by CreationTime
    $sortedFiles = Get-ChildItem -Path $FolderPath -File |
                   Where-Object { $_.CreationTime.Month -eq $Month -and $_.CreationTime.Year -eq $Year } |
                   Sort-Object CreationTime

    return $sortedFiles
}
#TODO: change this chrono
$START_CHRONO = Get-Date "1/11/2023"
$file_name = "Csv3.csv"

try{
    $file = Get-Item (Join-Path $FOLDER_PATH $file_name) -ErrorAction Stop
}
catch{
    write-host $_
    Write-Host -1
    exit
}
Write-Host $file#

$file_date = $file.CreationTime

$ser1 = (difference -ds2 $START_CHRONO -ds1 $file_date )+1
Write-Host $ser1#

$file_arr = Get-SortedFilesByMonth -Month $file_date.Month -Year $file_date.Year
Write-Host $file_arr#
$ser2 = 1
foreach ($f in $file_arr){
    if ($f.Name -ne $file.Name){
        $ser2 ++
    }else {
        break
    }
}
Write-Host $ser2
$serial_num = [string]$ser1+"."+[string]$ser2
Write-Host $serial_num
