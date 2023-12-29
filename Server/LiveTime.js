function display_ct7() {
    var x = new Date()

    // HH/MM/SS
    var ampm = x.getHours( ) >= 12 ? ' CH' : ' SA';
    hours = x.getHours( ) % 12;
    hours = hours ? hours : 12;
    hours=hours.toString().length==1? 0+hours.toString() : hours;

    var minutes=x.getMinutes().toString()
    minutes=minutes.length==1 ? 0+minutes : minutes;

    var seconds=x.getSeconds().toString()
    seconds=seconds.length==1 ? 0+seconds : seconds;

    // DD/MM/YY
    var dt=x.getDate().toString();
    dt=dt.length==1 ? 0+dt : dt;

    var month=(x.getMonth() +1).toString();
    month=month.length==1 ? 0+month : month;

    var x1= dt + "/" + month + "/" + x.getFullYear(); 
    x1 = x1 + " - " +  hours + ":" +  minutes + ":" +  seconds + " " + ampm;
    document.getElementById('ct7').innerHTML = x1;
    display_c7();
    }
    function display_c7(){
    var refresh=1000; // Refresh rate in milli seconds
    mytime=setTimeout('display_ct7()',refresh)
}
display_c7()