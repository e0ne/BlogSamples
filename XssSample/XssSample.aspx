<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="XssSample.aspx.cs" Inherits="XssSample.XssSample" ValidateRequest="false" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>XSS Sample</title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
		<asp:TextBox ID="tbText" runat="server" Text="<script>alert('This is XSS attack');</script>" /> <asp:Button ID="btnSubmit" OnClick="btnSubmitOnClick" runat="server" Text="Submit"/>
    </div>
	<div>
		<asp:Literal ID="litText" runat="server" />
	</div>
    </form>
</body>
</html>
