using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace map_cs
{
    static class Program
    {
        /// <summary>
        ///  The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.SetHighDpiMode(HighDpiMode.SystemAware);
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new Form1());
        }
    }
}

namespace My_tools
{
    public class Exec
    {
        public static string ExecCMD(string command)
        {
            System.Diagnostics.Process pro = new System.Diagnostics.Process();
            pro.StartInfo.FileName = "cmd.exe";
            pro.StartInfo.UseShellExecute = false;
            pro.StartInfo.RedirectStandardError = true;
            pro.StartInfo.RedirectStandardInput = true;
            pro.StartInfo.RedirectStandardOutput = true;
            pro.StartInfo.CreateNoWindow = true;
            //pro.StartInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden;
            pro.Start();
            pro.StandardInput.WriteLine(command);
            pro.StandardInput.WriteLine("exit");
            pro.StandardInput.AutoFlush = true;
            
            string output = pro.StandardOutput.ReadToEnd();
            pro.WaitForExit();
            pro.Close();
            return output;
        }


        private static string CMDPath = Environment.GetFolderPath(Environment.SpecialFolder.System) + "\\cmd.exe";

        public static string RunCMDCommand(string Command)
        {
            
            using (System.Diagnostics.Process pc = new System.Diagnostics.Process())
            {
                String OutPut;
                Command = Command.Trim().TrimEnd('&') + "&exit";

                pc.StartInfo.FileName = CMDPath;
                pc.StartInfo.CreateNoWindow = true;
                pc.StartInfo.RedirectStandardError = true;
                pc.StartInfo.RedirectStandardInput = true;
                pc.StartInfo.RedirectStandardOutput = true;
                pc.StartInfo.UseShellExecute = false;

                pc.Start();

                pc.StandardInput.WriteLine(Command);
                pc.StandardInput.AutoFlush = true;

                OutPut = pc.StandardOutput.ReadToEnd();
                int P = OutPut.IndexOf(Command) + Command.Length;
                OutPut = OutPut.Substring(P, OutPut.Length - P - 2);
                pc.WaitForExit();
                pc.Close();
                return OutPut;
            }
        }

    }
    public class Show
    {
        public static void ShowImage(String picName)
        {

            //建立新的系统进程 
            System.Diagnostics.Process process = new System.Diagnostics.Process();
            //设置文件名，此处为图片的真实路径+文件名 
            process.StartInfo.FileName = picName;
            //此为关键部分。设置进程运行参数，此时为最大化窗口显示图片。 
            process.StartInfo.Arguments = "rundll32.exe C:\\WINDOWS\\system32\\shimgvw.dll,ImageView_Fullscreen";
            //此项为是否使用Shell执行程序，因系统默认为true，此项也可不设，但若设置必须为true 
            process.StartInfo.UseShellExecute = true;
            //此处可以更改进程所打开窗体的显示样式，可以不设 
            process.StartInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden;
            process.Start();
            process.Close();
        }
    }
}

