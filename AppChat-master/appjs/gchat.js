angular.module('AppChat').controller('GChatController', ['$http', '$log', '$scope','$location', '$routeParams', 
    function($http, $log, $scope, $location, $routeParams) {
        var thisCtrl = this;
        $scope.nowdate = Date();
        
        this.messageList = [];
        this.counter  = 2;
        this.newText = "";
        this.newMessageList = [];
        
        var id = 0;
        //var uid = $routeParams.uid;
        //var gid = $routeParams.gid;
        //console.log("route userd Id: " +$routeParams.uid);
        //console.log("route group Id: "+$routeParams.gid);
            
            
            //console.log("userd Id: " +this.uid);
            //console.log("group Id: "+this.gid);
        
       this.loadMessages = function(){
            // Get the list of parts from the servers via REST API
            var userid = $routeParams.uid;
            var groupid = $routeParams.gid;
            
            // First set up the url for te route
            var url = "http://localhost:5000/MessagingAppP1/group/"+groupid+"/messages";
            // Now set up the $http object
            // It has two function call backs, one for success and one for error
            $http.get(url).then(// success call back
                function (response){
                // The is the sucess function!
                // Copy the list of parts in the data variable
                // into the list of parts in the controller.

                    console.log("response1: " + JSON.stringify(response));
                    
                    thisCtrl.messageList = response.data.GroupMessages;

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
        
        
       this.postMessage = function(){
           
           var data = {};
            //get message info
            var info = thisCtrl.newText;
            
            //Getting message date
            var date = $scope.nowdate;
            
            console.log("newText: "+thisCtrl.newText);
            console.log("info: "+this.info);
            data.mdate = $scope.nowdate;
            data.minfo = thisCtrl.newText;
            data.uid = $routeParams.uid;
        
            
            //data.udescription = this.description;
            
            console.log("data: " + JSON.stringify(data));
            // Now create the url with the route to talk with the rest API
            var reqURL = "http://localhost:5000/MessagingAppP1/messages";
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
                    alert("New user added with id: " +response.data.User.mid);
                    
                    thisCtrl.id = response.data.User.mid
                    
                    console.log("ctrl cid "+this.id )
                    
                    thisCtrl.newMessagelList = response.data.User;
                    
                    console.log("thiscredentialList: " +JSON.stringify(thisCtrl.newMessageList))
                    
                    console.log("second sign in")
                    thisCtrl.messageIsPart();
                   
                    
                }, //Error function
                function (response) {
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
                    var status = response.status;
                    console.log("thiscredentialList: " +JSON.stringify(thisCtrl.newMessageList));
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
        
        this.messageIsPart = function(){
            // Get the target part id from the parameter in the url
            // using the $routerParams object
            //var userId = $routeParams.uid;
            console.log("Howdy")
            var data = {};
            
            console.log("cid: "+this.id);
            console.log("ctrl cid: "+thisCtrl.id);
            
            data.mid = this.id;
            data.gid = $routeParams.gid;
            
            console.log("data: " + JSON.stringify(data));
            
            // Now create the url with the route to talk with the rest API
            var reqURL = "http://localhost:5000/MessagingAppP1/PartOfGroup";
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
                    //alert("New user added with id: " +response.data.);
                    //$location.url('/login');
                    
                }, //Error function
                function (response) {
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
                    var status = response.status;
                    console.log("thiscredentialList: " +JSON.stringify(thisCtrl.newMessageList));
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
        
        
        this.messageRating = function (mid) {
            $location.url('/messagerating/' + mid);
        };
        
        this.loginRedirect= function(){
            $location.url('/login');
        };
        
        this.realod = function(){
            location.reload();
        }
            
        this.loadMessages();
}]);
