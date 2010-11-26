using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace XssSample
{
	public partial class XssSample : Page
	{
		protected void btnSubmitOnClick(object sender, EventArgs e)
		{
			this.litText.Text = this.tbText.Text;
		}
	}
}