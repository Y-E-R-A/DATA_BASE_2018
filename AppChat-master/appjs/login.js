/**
 * Created by manuel on 4/24/18.
 */
angular.module('AppChat').controller('LoginController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {
        // This variable lets you access this controller
        // from within the callbacks of the $http object

        var thisCtrl = this;
        
        var user = "";
        
        var password = "";

        // This variable hold the information on the part
        // as read from the REST API
        var credentialList = {};

        this.loginUser = function(){
            // Get the target part id from the parameter in the url
            // using the $routerParams object
            //var userId = $routeParams.uid;
            
            var data = {};
        
            data.cuser = this.user;
            
            data.cpassword = this.password;
            
            console.log("data: " + JSON.stringify(data));
            console.log("user: "+this.user);
            console.log("password: "+this.password);
            
            // Now create the url with the route to talk with the rest API
            var reqURL = "http://localhost:5000/MessagingAppP1/credentials/user";
            console.log("reqURL: " + reqURL);
            var config = { headers : 
                          {'Content-Type':'application/json;charset=utf-8;' }
                         }
        
            // Now issue the http request to the rest API
            $http.post(reqURL,data,config).then(
                // Success function
                function (response) {
                    console.log("response: " + JSON.stringify(response.data))
                    // assing the part details to the variable in the controller
                     thisCtrl.credentialsList = response.data.User;
                     console.log("thiscredentialList: " +JSON.stringify(thisCtrl.credentialsList))
                    console.log("uid without JSON: " + response.data.User)
                    //this.group(response.data.User.uid);
                    console.log("uid: " + JSON.stringify(response.data.User[0].uid))
                    
                    $location.url('/group/' + response.data.User[0].uid);
                    
                }, //Error function
                function (response) {
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
                    var status = response.status;
                    console.log("thiscredentialList: " +JSON.stringify(thisCtrl.credentialsList));
                    //console.log("Error: " + reqURL);
                    //alert("Cristo");
                    if (status == 0) {
                        alert("No hay conexion a Internet");
                    }
                    else if (status == 401) {
                        alert("Su sesion expiro. Conectese de nuevo.");
                    }
                    else if (status == 403) {
                        alert("No esta autorizado a usar el sistema.");
                    }
                    else if (status == 404) {
                        alert("No se encontro la informacion solicitada.");
                    }
                    else {
                        alert("Error interno del sistema.");
                    }
                }
            );
        };
        //this.loginUser();
       // this.group = function (uid) {
        //    $location.url('/group/' + uid);
        //};
        this.signupRedirect = function(){
            $location.url('/signup');
        }
        
}]);