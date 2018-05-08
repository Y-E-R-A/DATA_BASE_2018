/**
 * Created by manuel on 4/24/18.
 */
angular.module('AppChat').controller('MessageRatingController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {
        // This variable lets you access this controller
        // from within the callbacks of the $http object

        var thisCtrl = this;

        // This variable hold the information on the part
        // as read from the REST API
        var messageRating = {};

        this.loadRatings = function(){
            // Get the target part id from the parameter in the url
            // using the $routerParams object
            var messageId = $routeParams.mid;

            // Now create the url with the route to talk with the rest API
            var reqURL = "http://localhost:5000/MessagingAppP1/message/"+messageId+"/users/";
            console.log("mid " + messageId);
            console.log("reqURL: " + reqURL);
           
            // Now issue the http request to the rest API
            $http.get(reqURL).then(
                // Success function
                function (response) {
                    console.log("response: " + JSON.stringify(response))
                    // assing the part details to the variable in the controller
                     thisCtrl.messageRating = response.data.Reaction;
           
                }, //Error function
                function (response) {
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
                    var status = response.status;
                    console.log("thismessageRating: " +JSON.stringify(thisCtrl.messageRating));
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

        this.loadRatings();
}]);