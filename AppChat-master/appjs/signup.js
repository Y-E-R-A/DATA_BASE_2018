/**
 * Created by manuel on 4/24/18.
 */
angular.module('AppChat').controller('SignUpController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {
        // This variable lets you access this controller
        // from within the callbacks of the $http object

        var thisCtrl = this;
        
        var first_name = "";
        
        var last_name = "";
        
        var user_name = "";
        
        var password = "";
        
        var email = "";
        
        var phone = "";
        
        var description = "";
            
        var id = 0;
        // This variable hold the information on the part
        // as read from the REST API
        var credentialList = {};
        
    
        
        this.signUpCredentials = function(){
            // Get the target part id from the parameter in the url
            // using the $routerParams object
            //var userId = $routeParams.uid;
            
            var data = {};
        
                     
            data.cuser_name = this.user_name;
            
            data.cpassword = this.password;
            
            data.cemail = this.email;
        
            
            //data.udescription = this.description;
            
            console.log("data: " + JSON.stringify(data));
            console.log("first name: "+this.first_name);
            console.log("last name: "+this.last_name);
            // Now create the url with the route to talk with the rest API
            var reqURL = "http://localhost:5000/MessagingAppP1/credentials";
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
                    alert("New user added with id: " +response.data.User.cid);
                    
                    thisCtrl.id = response.data.User.cid
                    
                    console.log("ctrl cid "+this.id )
                    
                    thisCtrl.credentialList = response.data.User;
                    
                    console.log("thiscredentialList: " +JSON.stringify(thisCtrl.credentialList))
                    
                    console.log("second sign in")
                    
                    thisCtrl.signUpUser();
                    
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
        
        this.signUpUser = function(){
            // Get the target part id from the parameter in the url
            // using the $routerParams object
            //var userId = $routeParams.uid;
            console.log("Howdy")
            var data = {};
            
            console.log("cid: "+this.id);
            console.log("ctrl cid: "+thisCtrl.id);
            data.cid = this.id;
            
            //data.cid = thisCtrl.id;
            
            data.ufirst_name = this.first_name;
            
            data.ulast_name = this.last_name;  
            
            data.uphone = this.phone;
            
            data.udescription = this.description;
            
            console.log("data: " + JSON.stringify(data));
            
            // Now create the url with the route to talk with the rest API
            var reqURL = "http://localhost:5000/MessagingAppP1/user";
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
                    alert("New user added with id: " +response.data.User.uid);
                    $location.url('/login');
                    
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
        this.signUp = function(){
            console.log('first credentials')
            this.signUpCredentials();
                
            //console.log("cid "+ this.cid)
            //console.log('second user')
            //this.signUpUser();
        };
        
}]);