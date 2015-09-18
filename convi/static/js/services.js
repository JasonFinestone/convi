'use strict';

var convertServices = angular.module('convertServices', []);

convertServices.service("convertInfoService", ['$cookieStore', function($cookieStore) {
    //this.convertInfo = {}

    this.setConvertInfo = function(data) {
        //return this.user = data;
        //this.user = $cookieStore.put("user",data);
        return this.convertInfo = $cookieStore.put('convertInfo',data);
    };
     
    this.getConvertInfo = function() {
      //return this.user;
      //this.user = $cookieStore.get('user');
      return this.convertInfo = $cookieStore.get('convertInfo');
    };

    this.getConvertMatch = function(){
    	this.convertInfo = $cookieStore.get('convertInfo');
    	return this.convertInfo.fix.concat(" ",this.convertInfo.vtmf);
    };

    this.removeConvertInfo = function() {
      return this.convertInfo = $cookieStore.remove('convertInfo');
    };
 }]);
