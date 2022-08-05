var correctans = 0;
var wrong = 0; 
var timer;

function check_color (name, correct)
{
	const div_data = document.getElementsByName(name.toString());
	var value_entered = div_data[0].value;
	// console.log(value_entered);
	const corr = correct.toString();
	if(value_entered === corr){
		correctans = correctans +1;
		div_data[0].className = "def-text-input green"; 
		document.getElementById("showcorrect").innerHTML = "Correct : "+correctans;
	} else if (value_entered != "")
	{
		wrong = wrong + 1;
		div_data[0].className = "def-text-input red";
		document.getElementById("showwrong").innerHTML = "Wrong : "+wrong;
	}
}
var time = 0;

function startTimer()
{	var hh, mm, ss;
	var navs = document.getElementsByTagName("a");
	var btns = document.getElementsByName("valu");
	for (let i=0; i < navs.length; i++)
	{
		var href = navs[i].href;    
        navs[i].setAttribute("rel", href);    
        navs[i].href = "javascript:";
	}
	for (let i=0; i < btns.length; i++)
	{
		btns[i].disabled = true;
		// console.log(btns[i]);
	}

	timer = setInterval(function() {
		time = time + 1;
		hh = Math.floor(time/3600)
		mm = Math.floor(time/60)%60
		ss = time%60
		hh = (hh < 10) ? "0" + hh : hh;
		mm = (mm < 10) ? "0" + mm : mm;
		ss = (ss < 10) ? "0" + ss : ss;
		document.getElementById("showtime").innerHTML = "Timer : " + hh + ":" + mm + ":" + ss ;
		// console.log(time);
	}, 1000)
}

function stopTimer(zeros)
{
	clearInterval(timer);
	var navs = document.getElementsByTagName("a");
	var btns = document.getElementsByName("valu");
	for (let i=0; i < navs.length; i++)
	{
		var href = navs[i].getAttribute("rel");    
        navs[i].removeAttribute("rel");    
        navs[i].href = href;
	}
	for (let i=0; i < btns.length; i++)
	{
		btns[i].disabled = false;
		// console.log(btns[i]);
	}
	score = Math.max(correctans*2 - wrong*5 - zeros, 0);

	// console.log(time)
}

