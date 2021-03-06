angular.module('AppChat').controller('AddParticipantController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {
        // This variable lets you access this controller
        // from within the callbacks of the $http object

        var thisCtrl = this;
        var participant_phone = "";
        var gid = $routeParams.gid;
      
        
        
        // This variable hold the information on the part
        // as read from the REST API
        var participantList= {};
        var admindata = {};
        
        var cuid = 0;
        this.adminPriviledges = function(){
            // Get the target part id from the parameter in the url
            // using the $routerParams object
            var group_admin = $routeParams.uid;
            console.log("Administrator ID: " + group_admin);

            // Now create the url with the route to talk with the rest API
            var reqURL = "http://localhost:5000/MessagingAppP1/Admin/"+group_admin;
            
            console.log("reqURL: " + reqURL);

            // Now issue the http request to the rest API
            $http.get(reqURL).then(
                // Success function
                function (response) {
                    console.log("response: " + JSON.stringify(response))
                    console.log("Check UID of contact");

                    thisCtrl.admindata = response.data.Admin;
                    console.log("uid: "+ $routeParams.uid);
                    if($routeParams.uid == response.data.Admin.uid){
                        console.log("Admin");
                        thisCtrl.userIDByPhone();
                    }else{
                        alert("not Administrator");
                    }


                }, //Error function
                function (response) {
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
                    var status = response.status;
                    console.log("Unable to perform operation");

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

         this.userIDByPhone = function(){
            // Get the target part id from the parameter in the url
            // using the $routerParams object

            console.log("Finding User ID with phone: " + thisCtrl.participant_phone);

            // Now create the url with the route to talk with the rest API
            var reqURL = "http://localhost:5000/MessagingAppP1/uid/"+thisCtrl.participant_phone;

            console.log("reqURL: " + reqURL);
           
            // Now issue the http request to the rest API
            $http.get(reqURL).then(
                // Success function
                function (response) {
                    console.log("response: " + JSON.stringify(response))
                   
                    thisCtrl.cuid= response.data.User[0].uid;

                    thisCtrl.participantList=response.data;

                    thisCtrl.invite_participant();
                    
                    
                }, //Error function
                function (response) {
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
                    var status = response.status;
                    console.log("Unable to perform operation");
                    
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
        
        
        this.invite_participant  = function(){
            // Get the target part id from the parameter in the url
            // using the $routerParams object
            //var userId = $routeParams.uid;
            var data = {};
                         

            data.gid = $routeParams.gid;
            data.uid= this.cuid;
            console.log("cuid: "+this.cuid)
            console.log("data: " + JSON.stringify(data));
            
            
            // Now create the url with the route to talk with the rest API
            var reqURL = "http://localhost:5000/MessagingAppP1/GroupParticipants"
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
                    alert("New participant added ");
                    
                    thisCtrl.participantList = response.data;
                    
                    console.log("thisgParticipationList: " +JSON.stringify(thisCtrl.participantList))
                   
                    
                                       
                }, //Error function
                function (response) {
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
                    var status = response.status;
                    console.log("thisparticipantList: " +JSON.stringify(thisCtrl.participantList));
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

        this.Back= function(){
            $location.url('/gchat/'+$routeParams.uid+'/'+$routeParams.gid);
        }

}


]);