var state = false;
var socket;

var opt = {
  "type": "basic",
  "title": "Phone SMS",
  "message": "",
  "iconUrl": "images/msg.png"
};

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("toggle").addEventListener("click",function(){
	    if (state == false){
	    	// Initiate socket connection
	    	if (typeof socket == undefined || socket == null || !socket.connected){
		    	socket = io.connect('http://localhost:5000/?key=ZaxtfTpNj0mV3fZ0GlWdktKj8SpiBS0gRBXVNIMUR5NZms1w3K'); 	
		    	console.log("Socket opened");
		    	state = true;
	    		document.getElementById("toggle").src = "images/on.png";

		    	socket.on('notification', function (msg) {
		    		console.log("Received msg");
		    		console.log(msg.data)
		    		opt.message = msg.data
		    		console.log(opt)
					chrome.notifications.create(new Date().getTime().toString(), opt);
				});

	    	}

	    }
	    else{
	    	state = false;
	    	document.getElementById("toggle").src = "images/off.png";

	    	// Close socket connection
	    	if (typeof socket != undefined && socket != null && socket.connected){
		    	socket.close();
		    	console.log("Socket closed");

	    	}

	    }
	});
});

