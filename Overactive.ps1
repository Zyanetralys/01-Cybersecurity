param(
    [int]$Intervalo = 5,
    [int]$DuracionClick = 30
)

Add-Type @"
using System;
using System.ComponentModel;
using System.Runtime.InteropServices;

public class AutoClicker
{
    [StructLayout(LayoutKind.Sequential)]
    struct INPUT
    {
        public int type;
        public MOUSEINPUT mi;
    }

    [StructLayout(LayoutKind.Sequential)]
    struct MOUSEINPUT
    {
        public int dx;
        public int dy;
        public uint mouseData;
        public uint dwFlags;
        public uint time;
        public IntPtr dwExtraInfo;
    }

    const int INPUT_MOUSE = 0;
    const uint MOUSEEVENTF_LEFTDOWN = 0x0002;
    const uint MOUSEEVENTF_LEFTUP   = 0x0004;

    [DllImport("user32.dll", SetLastError=true)]
    static extern uint SendInput(uint nInputs, INPUT[] pInputs, int cbSize);

    public static void Click(int durationMs)
    {
        INPUT down = new INPUT();
        down.type = INPUT_MOUSE;
        down.mi.dwFlags = MOUSEEVENTF_LEFTDOWN;

        INPUT up = new INPUT();
        up.type = INPUT_MOUSE;
        up.mi.dwFlags = MOUSEEVENTF_LEFTUP;

        int size = Marshal.SizeOf<INPUT>();

        if (SendInput(1, new INPUT[] { down }, size) == 0)
            throw new Win32Exception();

        System.Threading.Thread.Sleep(durationMs);

        if (SendInput(1, new INPUT[] { up }, size) == 0)
            throw new Win32Exception();
    }

    [DllImport("user32.dll")]
    public static extern short GetAsyncKeyState(int vKey);
}
"@

Write-Host "Autoclicker iniciado. F8 para salir.`n"

while ($true)
{
    [AutoClicker]::Click($DuracionClick)
    Write-Host "$(Get-Date -Format 'HH:mm:ss') -> cript"

    $espera = ($Intervalo * 1000) - $DuracionClick
    if ($espera -lt 0) { $espera = 0 }

    for ($i = 0; $i -lt [math]::Ceiling($espera / 100); $i++)
    {
        if(([AutoClicker]::GetAsyncKeyState(0x77) -band 0x8000) -ne 0)
        {
            Write-Host "Autoclicker detenido."
            return
        }

        $restante = $espera - ($i * 100)
        Start-Sleep -Milliseconds ([Math]::Min(100, $restante))
    }
}
