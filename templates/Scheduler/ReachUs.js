function updateContact(){
	var contact= document.getElementById('diningHall').innerHTML;
	var pic = new Image(100,100);
	if(contact == "Sadler")
	{
		pic.src = "Scheduler/DGriffo.jpg";
		document.getElementById("address1").innerHTML = "100 Irving Ave";
		document.getElementById("address2").innerHTML = "Sadler Hall";
		document.getElementById("phone").innerHTML ="315-443-2449";
		document.getElementById("manager").innerHTML ="Debbie Lawson";
		document.getElementById("email").innerHTML ="dgriffo@syr.edu";
	}
	
	else if(contact == "Shaw")
	{
		
		pic.src = "Scheduler/SBrandt.jpg";
		document.getElementById("address1").innerHTML = "201 Euclid Ave";
		document.getElementById("address2").innerHTML = "Shaw Hall";
		document.getElementById("phone").innerHTML ="315-443-2383";
		document.getElementById("manager").innerHTML ="Stephen Brandt";
		document.getElementById("email").innerHTML ="sjbrandt@syr.edu";
	}
	
	
	else if(contact == "Graham")
	{
		pic.src = "Scheduler/KHellinger.jpg";
		document.getElementById("address1").innerHTML = "Mt. Olympus Drive";
		document.getElementById("address2").innerHTML = "Between Flint & Day Halls";
		document.getElementById("phone").innerHTML ="315-443-2421";
		document.getElementById("manager").innerHTML ="Kathy Hellinger";
		document.getElementById("email").innerHTML ="kmhellin@syr.edu";
	}
	
	
	else if(contact == "Brockway")
	{
		pic.src = "Scheduler/JBlackmon.jpg";
		document.getElementById("address1").innerHTML = "401 Van Buren Street ";
		document.getElementById("address2").innerHTML = "Brewster/Boland/Brockway";
		document.getElementById("phone").innerHTML ="315-443-3069";
		document.getElementById("manager").innerHTML ="James Blackmon";
		document.getElementById("email").innerHTML ="jjblackm@syr.edu";
	}
	
	
	else if(contact == "Ernie Davis")
	{
		
		pic.src = "Scheduler/Brandt.jpg";
		document.getElementById("address1").innerHTML = "601 Comstock Ave";
		document.getElementById("address2").innerHTML = "Ernie Davis";
		document.getElementById("phone").innerHTML ="315-443-1450";
		document.getElementById("manager").innerHTML ="Stephen Brandt";
		document.getElementById("email").innerHTML ="sjbrandt@syr.edu";
	}
	
	document.getElementById('managerPic').src = pic.src;
}