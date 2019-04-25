
        //API request for tour dates from Resident Advisor 
        var request = new XMLHttpRequest();
        request.open("GET",'https://www.residentadvisor.net/api/events.asmx/GetEvents?AccessKey=ed0e7f28-e01b-4dfc-b0e1-47b79a49ecec&UserID=360584&DJID=77328&Option=1&VenueID=&CountryID=&AreaID=&PromoterID=&Year=', true);
        
        request.responseType = 'document';

        request.overrideMimeType('text/xml');

        request.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200){
                myFunction(this);
                console.log(request.response, request.responseXML);
            }
        };

        function myFunction(xml){
            var venue, date, area, title, i, date_c, venue_c, area_c, title_c, xmlDoc;
            xmlDoc = xml.responseXML;
            date_c = "";
            venue_c = "" ;
            area_c = "";
            //title_c = "";
            date = xmlDoc.getElementsByTagName("eventdate")
            for (i=0; i<date.length; i++){
                date_c += date[i].childNodes[0].nodeValue.substring(2,10)+ "<br>";
            }
            
            /*title = xmlDoc.getElementsByTagName("title")
            for (i=0; i<title.length; i++){
                title_c += title[i].childNodes[0].nodeValue.substring(0,50)+ "<br>";
            }*/
            venue = xmlDoc.getElementsByTagName("venue")
            for (i = 0; i < venue.length; i++){
                venue_c += venue[i].childNodes[0].nodeValue + "<br>";
            }
            area = xmlDoc.getElementsByTagName("areaname")
            for (i=0; i<area.length; i++){
                area_c += area[i].childNodes[0].nodeValue.substring(0,10)+ "<br>";
            }

            document.getElementById("upcoming_date").innerHTML = date_c;
            
            //document.getElementById("title").innerHTML = title_c;
            document.getElementById("upcoming_venue").innerHTML = venue_c;
            document.getElementById("upcoming_area").innerHTML = area_c;

            
            
        }
        
        request.send();