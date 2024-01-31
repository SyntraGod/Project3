// TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  const firebaseConfig = {
    apiKey: "AIzaSyA2Qj0QFseWKOTf0leS1xUlbh_SmGoH-Zs",
    authDomain: "projectcameradata.firebaseapp.com",
    databaseURL: "https://projectcameradata-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "projectcameradata",
    storageBucket: "projectcameradata.appspot.com",
    messagingSenderId: "91717495355",
    appId: "1:91717495355:web:5ee61c2ee67051986f8a1e"
  };

  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  var database = firebase.database();
  var passengerInValue = 0;
  var passengerOutValue = 0;

  // Get the number of passengers getting in the bus
  function getPassengerIn() {
    return Promise.all([
      database.ref("/0001/numIn").once("value"),
      database.ref("/0002/numIn").once("value")
    ]).then(function (snapshots) {
      var value1 = snapshots[0].val() || 0;
      var value2 = snapshots[1].val() || 0;
      passengerInValue = value1 + value2;
      document.getElementById("numberIn").innerHTML = passengerInValue;
    }).catch(function (error) {
      console.error("Error getting passengerIn values:", error);
    });
  }
  setInterval(getPassengerIn, 1000);

  // Get the number of passengers getting out of the bus
  function getPassengerOut() {
    return Promise.all([
      database.ref("/0001/numOut").once("value"),
      database.ref("/0002/numOut").once("value")
    ]).then(function (snapshots) {
      var value1 = snapshots[0].val() || 0;
      var value2 = snapshots[1].val() || 0;
      passengerOutValue = value1 + value2;
      document.getElementById("numberOut").innerHTML = passengerOutValue;
    }).catch(function (error) {
      console.error("Error getting passengerOut values:", error);
    });
  }
  setInterval(getPassengerOut, 1000);

  // Subtract the values and update the result
  function updateCurPassenger() {
    var curPassenger = passengerInValue - passengerOutValue;
    document.getElementById("numberCur").innerHTML = curPassenger;
  }

  // Call the updateDifference function every second
  setInterval(updateCurPassenger, 100);


  // ---------------------Camera Status----------------
  //Front door
  database.ref("/0001/camStatus").on("value", function(snapshot){
    var status = snapshot.val();
    if(status == 1){
      document.getElementById("cam1").innerHTML = "Open";
    }
    else {
      document.getElementById("cam1").innerHTML = "Close";
    }
  });
  //Rear door
  database.ref("/0002/camStatus").on("value", function(snapshot){
    var status = snapshot.val();
    if(status == 1){
      document.getElementById("cam2").innerHTML = "Open";
    }
    else {
      document.getElementById("cam2").innerHTML = "Close";
    }
  });


  //----------------Door Status----------------
  //Front door
  database.ref("/0001/doorStatus").on("value", function(snapshot){
    var status = snapshot.val();
    if(status == 0){
      document.getElementById("frontDoorStatus").innerHTML = "Open";
    }
    else {
      document.getElementById("frontDoorStatus").innerHTML = "Close";
    }
  });
  //Rear door
  database.ref("/0002/doorStatus").on("value", function(snapshot){
    var status = snapshot.val();
    if(status == 0){
      document.getElementById("rearDoorStatus").innerHTML = "Open";
    }
    else {
      document.getElementById("rearDoorStatus").innerHTML = "Close";
    }
  });