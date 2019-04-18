




function loadXMLDoc(){
    var request = new XMLHttpRequest();
    request.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        myFunction(this);
      }
    };
    request.open("GET", 'https://www.residentadvisor.net/api/events.asmx/GetEvents?AccessKey=ed0e7f28-e01b-4dfc-b0e1-47b79a49ecec&UserID=360584&DJID=77328&Option=1&VenueID=&CountryID=&AreaID=&PromoterID=&Year=', true);
    request.send();
  }
  
  function myFunction(xml) {
    var x, i, xmlDoc, txt;
    xmlDoc = xml.responseXML;
    txt = "";
    x = xmlDoc.getElementsByTagName("eventdate");
    for (i = 0; i< x.length; i++) {
      txt += x[i].childNodes[0].nodeValue + "<br>";
    }
    document.getElementById("demo").innerHTML = txt;
  }


  // Begin accessing JSON data here
var data = JSON.parse(this.response)

if (request.status >= 200 && request.status < 400) {
  data.forEach(movie => {
    console.log(movie.title)
  })
} else {
  console.log('error')
}
Here