  angular.module('AppChat').controller('SignUpController', ['$http', '$log', '$scope','$location',
    function($http, $log, $scope, $location) {
        var thisCtrl = this;
        $scope.nowdate = Date();
        
        this.credentialsList = [];
        this.counter  = 2;
        this.username = "";
        this.password ="";
        
        
        this.loadMessages = function(){
            // Get the list of parts from the servers via REST API

            // First set up the url for the route
            var url = "http://localhost:5000/MessagingAppP1/user"+username+"/credentials";
            // Now set up the $http object
            // It has two function call backs, one for success and one for error
            $http.get(url).then(// success call back
                function (response){
                // The is the sucess function!
                // Copy the list of parts in the data variable
                // into the list of parts in the controller.

                    console.log("response1: " + JSON.stringify(response));
                    
                    thisCtrl.credentialsList = response.data.Credentials;

                    console.log("credentialsList: " + JSON.stringify(thisCtrl.credentialsList));
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
            $log.error("Credentials Loaded: ", JSON.stringify(thisCtrl.credentialsList));
        };
        
         

        this.signup();
}]);
