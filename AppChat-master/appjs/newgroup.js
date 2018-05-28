angular.module('AppChat').controller('NewGroupController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {
        // This variable lets you access this controller
        // from within the callbacks of the $http object

        var thisCtrl = this;
        var group_name = "";
        var group_description = "";
        var id = 0;
        var group_admin = $routeParams.uid;
        
        
        // This variable hold the information on the part
        // as read from the REST API
        var data = {};
        var groupList = {};
        var participantList= {}
        var administratesList={}
                
        this.createNewGroup = function(){
            // Get the target part id from the parameter in the url
            // using the $routerParams object
            //var userId = $routeParams.uid;
            
            
        
            data.gName = this.group_name;
            data.gdescription = this.group_description;
            data.gcreation= Date();
            data.gadminID= $routeParams.uid;
            
                     
            console.log("data: " + JSON.stringify(data));
            console.log("group name: "+this.group_name);
            console.log("group description: "+this.group_description);
            
            
            
            // Now create the url with the route to talk with the rest API
            var reqURL = "http://localhost:5000/MessagingAppP1/groups"
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
                    alert("New group added with gid: " +response.data.Group.gid)
                    
                    thisCtrl.id = response.data.Group.gid
                    
                    console.log("ctrl id "+ response.data.Group.gid )
                    
                    console.log("ctrl adminID "+response.data.Group.uid )
                    
                    thisCtrl.groupList = response.data.Group;
                    
                    console.log("thisgroupList: " +JSON.stringify(thisCtrl.groupList))
                   
                    thisCtrl.updateAdministrator();
                              
                                       
                }, //Error function
                function (response) {
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
                    var status = response.status;
                    console.log("thisgroupList: " +JSON.stringify(thisCtrl.groupList));
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
        
        
        this.updateAdministrator =function(){
            console.log("Updating Administrate: "+ JSON.stringify(thisCtrl.groupList));
           
            var data = thisCtrl.groupList;
          
            administratesList= {};
            
             // Now create the url with the route to talk with the rest API
            var reqURL = "http://localhost:5000/MessagingAppP1/Admins"
            console.log("reqURL: " + reqURL);
            var config = { headers : 
                          {'Content-Type':'application/json;charset=utf-8;' }
                         }
           
            // Now issue the http request to the rest API
            $http.post(reqURL,data,config).then(
                // Success function
                function (response) {
                    
                    console.log("jsonificando YOMIIIIIIIIII: ")

                    // assing the part details to the variable in the controller
                    alert("New group administration event" );
                    thisCtrl.updateParticipation();                   
                                       
                }, //Error function
                function (response) {
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
                    var status = response.status;
                    console.log("thisAdministratesList: " +JSON.stringify(thisCtrl.groupList));
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
            
            
        )}
        
        
        
        this.updateParticipation  = function(){
            // Get the target part id from the parameter in the url
            // using the $routerParams object
            //var userId = $routeParams.uid;
            
            var data = thisCtrl.groupList;
                                 
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
}                                                         
]);

