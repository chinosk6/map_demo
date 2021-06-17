using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using My_tools;

namespace map_cs
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            String ret, c1, l1, c2, l2;
            c1 = textBox4.Text;
            l1 = textBox1.Text;
            c2 = textBox5.Text;
            l2 = textBox2.Text;
            if(c1 == "" || l1 == "" || c2 == "" || l2 == "")
            {
                MessageBox.Show("缺少必要参数");
                return;
            }

            String filename, retstr;
            String execmsg = "python map_bot.py " + "1" + " " + c1 + " " + l1 + " " + c2 + " " + l2; //1-路线规划

            //ret = My_tools.Exec.ExecCMD(execmsg);
            ret = My_tools.Exec.RunCMDCommand(execmsg);
            string[] retg = ret.Split("\n");
            if(retg.Length >= 4)
            {
                filename = retg[3];
                retstr = "起：" + retg[1] + "\n终：" + retg[2];
            }
            else
            {
                filename = "参数异常";
                retstr = "";
            }

            if(System.IO.File.Exists(filename))
            {
                //System.Diagnostics.Process.Start(filename);
                System.Threading.Thread.Sleep(500);
                My_tools.Show.ShowImage(filename);
                MessageBox.Show(retstr);
            }
            else
            {
                MessageBox.Show("处理异常:" + ret);
            }
            //MessageBox.Show(filename);
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void textBox3_TextChanged(object sender, EventArgs e)
        {

        }

        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {
            Form2 fm = new Form2();
            fm.ShowDialog();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            String ret, c1, l1;
            c1 = textBox6.Text;
            l1 = textBox3.Text;
            if (c1 == "" || l1 == "")
            {
                MessageBox.Show("缺少必要参数");
                return;
            }
            String filename;
            String execmsg = "python map_bot.py " + "2" + " " + c1 + " " + l1; //2-上车点推荐

            //ret = My_tools.Exec.ExecCMD(execmsg);
            ret = My_tools.Exec.RunCMDCommand(execmsg);
            string[] retg = ret.Split("\n");
            if (retg.Length >= 3)
            {
                filename = retg[2];             
            }
            else
            {
                filename = "参数异常";               
            }

            if (System.IO.File.Exists(filename))
            {
                System.Threading.Thread.Sleep(500);
                My_tools.Show.ShowImage(filename);
            }
            else
            {
                MessageBox.Show("处理异常:" + ret);
            }
            //MessageBox.Show(filename);
        }
    }
}
