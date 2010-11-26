using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace XssSample
{
	public partial class AntiXssSample : Page
	{
		protected void btnSubmitOnClick(object sender, EventArgs e)
		{
			this.litText.Text = Server.HtmlEncode(this.tbText.Text);
		}
	}
}