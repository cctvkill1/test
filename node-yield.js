 

var start = Date.now();
var a = [];
for (i = 0; i < 10000000; i++) {
	a[i] = i;
} 
var end = Date.now();
console.log(end - start);

// var co = require('hprose').co;


// co(function*() {
// 	try {
// 		var start = Date.now();
// 		var a = [];
// 		for (i = 0; i < 10000000; i++) {
// 			a[i] = i;
// 		}
// 		yield a;
// 		var end = Date.now();
// 		console.log(end - start);
// 	}
// 	catch (e) {
// 		console.error(e);
// 	}
// });

// var co = require('co');
// var co = require('hprose').co;
// var async = require('asyncawait/async');
// var await = require('asyncawait/await');
// co(function*() {
//     try {
//         var a = [];
//         for (i = 0; i < 1000000; i++) {
//             a[i] = i;
//         }
//         var start = Date.now();;
//         yield a;
//         var end = Date.now();;
//         console.log(end - start);
//     }
//     catch (e) {
//         console.error(e);
//     }
// });

// co(function*() {
//     try {
//         var a = [];
//         a[0] = a;
//         console.log(yield a);
//     }
//     catch (e) {
//         console.error(e);
//     }
// });

// co(function*() {
//     try {
//         var o = {};
//         o.self = o;
//         console.log(yield o);
//     }
//     catch (e) {
//         console.error(e);
//     }
// });

// (async function() {
//     try {
//         var a = [];
//         for (i = 0; i < 1000000; i++) {
//             a[i] = i;
//         }
//         var start = Date.now();
//         await a;
//         var end = Date.now();
//         console.log(end - start);
//     }
//     catch (e) {
//         console.error(e);
//     }
// })();

// (async function() {
//     try {
//         var a = [];
//         a[0] = a;
//         console.log(await a);
//     }
//     catch (e) {
//         console.error(e);
//     }
// })();

// (async function() {
//     try {
//         var o = {};
//         o.self = o;
//         console.log(await o);
//     }
//     catch (e) {
//         console.error(e);
//     }
// })();