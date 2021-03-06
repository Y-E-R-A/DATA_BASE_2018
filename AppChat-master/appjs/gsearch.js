angular.module('AppChat').controller('GSearchController', ['$http', '$log', '$scope','$location', '$routeParams', 
    function($http, $log, $scope, $location, $routeParams) {
        var thisCtrl = this;
        $scope.nowdate = Date();
        
        this.messageList = [];
        this.counter  = 2;
        this.newMessageList = [];
        this.hashList = [];
        var i = 0;
        this.searchMessage = function(){
           
            var info = thisCtrl.newText;
            
            //Getting message date
            var date = $scope.nowdate;

            
            //data.udescription = this.description;
            var reqURL = "http://localhost:5000/MessagingAppP1/group/"+$routeParams.gid+"/messages";
             
            console.log("reqURL: " + reqURL);
        
            // Now issue the http request to the rest API
            $http.get(reqURL).then(
                // Success function
                function (response) {
                    console.log("Messages");
                    console.log("response: " + JSON.stringify(response.data))
                    // assing the part details to the variable in the controller
                    

                    thisCtrl.newMessagelList = response.data.GroupMessages;
                    
                    console.log("thisNewMessageList: " +JSON.stringify(thisCtrl.newMessageList));
                    
                    console.log("response New Messa: " + JSON.stringify(response.data.GroupMessages))
                    
                    console.log("length: "+JSON.stringify(response.data.GroupMessages.length));
                    var i;
                    for(i =0; i<response.data.GroupMessages.length;i++){
                       console.log("string: "+ response.data.GroupMessages[i].minfo)
                        if(response.data.GroupMessages[i].minfo.includes("#")){
                           console.log("Contains #"); thisCtrl.hashList.push(response.data.GroupMessages[i]);
                        }
                    }
                    console.log("second sign in");
                    console.log("hashList: "+ JSON.stringify(thisCtrl.hashList));
                    //thisCtrl.messageIsPart (;
                   
                    
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
        this.searchMessage();
}]);
