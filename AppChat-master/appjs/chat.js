angular.module('AppChat').controller('ChatController', ['$http', '$log', '$scope','$location',
    function($http, $log, $scope, $location) {
        var thisCtrl = this;
        $scope.nowdate = Date();
        
        this.messageList = [];
        this.counter  = 2;
        this.newText = "";
        
        this.loadMessages = function(){
            // Get the list of parts from the servers via REST API

            // First set up the url for the route
            var url = "http://localhost:5000/MessagingAppP1/UserMessages";
            // Now set up the $http object
            // It has two function call backs, one for success and one for error
            $http.get(url).then(// success call back
                function (response){
                // The is the sucess function!
                // Copy the list of parts in the data variable
                // into the list of parts in the controller.

                    console.log("response1: " + JSON.stringify(response));
                    
                    thisCtrl.messageList = response.data.User;

                    console.log("msList: " + JSON.stringify(thisCtrl.messageList));
                }, // error callback
                function (response){
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
                    console.log("response2: " + JSON.stringify(response));
                    var status = response.status;
                    if (status == 0){
                        alert("No hay conexion a Internet");
                    }
                    else if (status == 401){
                        alert("Su sesion expiro. Conectese de nuevo.");
                    }
                    else if (status == 403){
                        alert("No esta autorizado a usar el sistema.");
                    }
                    else if (status == 404){
                        alert("No se encontro la informacion solicitada.");
                    }
                    else {
                        alert("Error interno del sistema.");
                    }
                }
            );
            $log.error("Message Loaded: ", JSON.stringify(thisCtrl.messageList));
        };
        this.postMsg = function(){
            
            var msg = thisCtrl.newText;
            // Need to figure out who I am
            var fecha = $scope.nowdate;
            var nextId = thisCtrl.counter++;
            thisCtrl.messageList.unshift({"uid": 1, "mid": nextId, "uName": "you", "mInfo": msg, "mDate": fecha, "like" : 0, "dislike" : 0});
            thisCtrl.newText = "";
        };
        this.messageRating = function (mid) {
            $location.url('/messagerating/' + mid);
        };
        
        this.loginRedirect= function(){
            $location.url('/login');
        };
        
        this.createGroupRedirect= function(){
            $location.url('/newgroup');
        };
            
        this.loadMessages();
}]);
