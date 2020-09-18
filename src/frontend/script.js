function fToC()
{
    num = document.getElementById(/*Fahrenheit Input ID*/).value;
    var xmlhttp = new XMLHttpRequest();
    var url = "https://TESTAPI.dlaff666.repl.co?F=" + num;
    xmlhttp.onreadystatechange = function()
    {
        if (this.readyState == 4 && this.status == 200)
        {
            var myArr = JSON.parse(this.responseText);
            printCResults(myArr);
        }
    };
    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}
function printCResults(arr)
{
    var out = "";
    out = arr.return;
    out = Math.round(out * 100)/100;
    document.getElementById(/*F to C Output ID*/).innerHTML = out + "&degC";
}

function cToF()
{
    num = document.getElementById(/*Celcius Input ID*/).value;
    var xmlhttp = new XMLHttpRequest();
    var url = "https://TESTAPI.dlaff666.repl.co?C=" + num;
    xmlhttp.onreadystatechange = function()
    {
        if (this.readyState == 4 && this.status == 200)
        {
            var myArr = JSON.parse(this.responseText);
            printFResults(myArr);
        }
    };
    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}
function printFResults(arr)
{
    var out = "";
    out = arr.return;
    out = Math.round(out * 100)/100;
    document.getElementById(/*C to F Output ID*/).innerHTML = out + "&degF";
}
