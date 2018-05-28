angular.module('AppChat').controller('ReplyController', ['$http', '$log', '$scope','$location', '$routeParams', 
    function($http, $log, $scope, $location, $routeParams) {
        var thisCtrl = this;
        $scope.nowdate = Date();
        
        this.messageList = [];
        this.counter  = 2;
        this.newText = "";
        this.newMessageList = [];
        
        var id = 0;
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
                     $location.url('/gchat/'+$routeParams.uid+'/'+$routeParams.gid);
                    
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
         this.replyToMessage = function(info){
           
           var data = {};
            //get message info
            var info = thisCtrl.newText;
            
            //Getting message date
            var date = $scope.nowdate;
            
            console.log("info: "+info);
            data.mdate = $scope.nowdate;
            data.minfo = "'RE: "+$routeParams.minfo+"', "+ info;
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
                    
                    console.log("thisNewMessageList: " +JSON.stringify(thisCtrl.newMessageList))
                    
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
        
        this.return = function(){
            $location.url('/gchat/'+$routeParams.uid+'/'+$routeParams.gid);
        }
        this.loginRedirect= function(){
            console.log("Log in");
            $location.url('/login');
        };
        
}]);
