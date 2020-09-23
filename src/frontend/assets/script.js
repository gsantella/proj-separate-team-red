function fToC()
{
    num = document.getElementById("inputFahrenheit").value;
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
    document.getElementById("outputFahrenheit").innerHTML = out;
}

function cToF()
{
    num = document.getElementById("inputCelsius").value;
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
    document.getElementById("outputCelsius").innerHTML = out;
}