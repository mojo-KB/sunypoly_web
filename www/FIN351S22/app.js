function createRequestObject() {
    var req;
    if (window.XMLHttpRequest) { // Firefox, Safari, Opera... 
        req = new XMLHttpRequest();
        //    alert('Detected a modern browser - very good!'); 
    } else if (window.ActiveXObject) { // Internet Explorer 5+ 
        req = new ActiveXObject("Microsoft.XMLHTTP");
        //    alert('Detected an old IE browser'); 
    } else {
        // error creating the request object, 
        // (maybe an old browser is being used?)
        alert('There was a problem creating the XMLHttpRequest object');
        req = '';
    }
    return req;
}



function sendRequest() {
    var now = new Date();
    //http.open('get', 'http://www.myhostname.com/cgi-bin/myscript.pl?nocache='+now.getTime()); 
    alert('before send');
    http.open('get', './cgi-bin/msg.cgi?nocache=' + now.getTime());

    //http.open('get', 'http://localhost:55555/cgi-bin/ajaxdemo.cgi?nocache='+now.getTime()); 
    //http.open('get', 'http://localhost/cgi-bin/ajaxdemo.cgi'); 
    http.onreadystatechange = handleResponse;
    http.send(null);
    alert("return");
}

function handleResponse() {
    if (http.readyState == 4 && http.status == 200) {
        //alert('in handleResponse');
        var response = http.responseText; // Text returned FROM perl script 
        if (response) { // UPDATE ajaxTest content 
            //alert('response was' + response);
            document.getElementById("ajaxstuff").innerHTML = response;
            //setTimeout('wipeout()', 5000); // wait 2 seconds, then clear message
        }
    }
}

function wipeout() {
    document.getElementById("ajaxstuff").innerHTML = '';
    x = document.getElementById("mybutton");
    x.disabled = false;
}

function doclick() {
    x = document.getElementById("mybutton");
    x.disabled = true;

    document.getElementById("ajaxstuff").innerHTML = '<b>working...</b>';
    sendRequest();
    return true;
}

function createRequestObject() {
    var req;
    if (window.XMLHttpRequest) { // Firefox, Safari, Opera...
        req = new XMLHttpRequest();
        //    alert('Detected a modern browser - very good!');
    } else if (window.ActiveXObject) { // Internet Explorer 5+
        req = new ActiveXObject("Microsoft.XMLHTTP");
        //    alert('Detected an old IE browser');
    } else {
        // error creating the request object,
        // (maybe an old browser is being used?)
        alert('There was a problem creating the XMLHttpRequest object');
        req = '';
    }
    return req;
}

// Make the XMLHttpRequest object
//var http = createRequestObject();
var myuser;

function dologin() {
    var now = new Date();
    myuser = document.getElementById("myinput").value;
    document.getElementById("username").innerHTML = myuser;;
    alert('dologin VALUE' + myuser);
    http.open('get', 'http://localhost:55555/cgi-bin/pick.cgi?myfunc=login&user=' + myuser + '&nocache=' + now.getTime());
    http.onreadystatechange = handleResponse1;
    http.send(null);
}

function doPostMessage() {
    var now = new Date();
    var mypost = document.getElementById("mypost").value;
    //document.getElementById("username").innerHTML = myuser;;
    //alert('dologin VALUE' + myuser);
    http.open('get', 'http://localhost:55555/cgi-bin/exammid.cgi?myfunc=post&mypost=' + mypost + '&user=' + myuser + '&nocache=' + now.getTime());
    http.onreadystatechange = handleResponse2;
    http.send(null);
}

function doGetMessages() {
    var now = new Date();
    var val;

    //var chkbxs = document.myradios["friend"];

    var thisform = document.forms['myradios'];

    //var chkbxs = document.getElementById("friend");
    var chkbxs = thisform['friend'];
    // loop through list of checkboxes
    for (var i = 0, len = chkbxs.length; i < len; i++) {
        //alert('getSelectVal=' + i + 'name=' + name);

        alert('getSelectVal=' + chkbxs[i].value);
        if (chkbxs[i].checked) { // chkbxs checked?
            if (defined(val)) {
                val = chkbxs[i].value; // if so, hold its value in val
            } else {
                val += ':' + chkbxs[i].value; // if so, hold its value in val
            }
            alert('found getSelectVal=' + val);
            //break; // and break out of for loop
        }
    }

    //document.getElementById("username").innerHTML = myuser;;
    alert('doGetMessages VALUE' + val);
    http.open('get', 'http://localhost:55555/cgi-bin/pick.cgi?myfunc=getfriendmsgs&friends=' + val + '&nocache=' + now.getTime());
    http.onreadystatechange = handleResponse3;
    http.send(null);
}

function handleResponse3() {
    if (http.readyState == 4 && http.status == 200) {
        var response = http.responseText; // Text returned FROM perl script 
        alert('friend messages' + response);
    }
}

function handleResponse2() {
    if (http.readyState == 4 && http.status == 200) {
        var response = http.responseText; // Text returned FROM perl script 
        alert('post message response' + response);
    }
}

function handleResponse1() {
    if (http.readyState == 4 && http.status == 200) {
        var response = http.responseText; // Text returned FROM perl script 
        var option;
        if (response) { // UPDATE ajaxTest content 
            response = response.replace(/&quot;/g, '"');
            //alert('Response1:' + response);

            //jsonData = JSON.parse(this.responseText);
            jsonData = JSON.parse(response);
            //alert('JSON DATA IS:' + jsonData);
            for (var i = 0; i < jsonData.length; i++) { // Start with 1 to skip the output directory name
                //alert(jsonData[i]);
                //option = new Option(jsonData[i], jsonData[i]);
                //$( "#single" ).append($(option));

                var myhtml = ' <input type="checkbox" id="friend" value="' +
                    jsonData[i] + '"  >' + jsonData[i] + '</input> \n';
                document.getElementById("myradios").innerHTML += myhtml;

                //alert('add innerhtml ' + myhtml);

                //<input type="radio" name="testcase" value="test1" id="testcase1" >test1</input>
            }
            $("#mainrow").show();
            $("#loginrow").hide();


            //document.getElementById("examplerunid").innerHTML = jsonData[0];
            //alert('BOX ID:' + document.getElementById("examplerunid"));

        }
    }
}