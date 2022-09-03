/*! For license information please see 2248.1b780e7a.chunk.js.LICENSE.txt */
"use strict";(self.webpackChunkinventory=self.webpackChunkinventory||[]).push([[2248],{87684:function(e,t,n){var r=n(15671),i=n(43144),a=n(39877),o=n(54318),c="http://5.182.47.38:8001/maintanance/",s=function(){function e(){(0,r.Z)(this,e)}return(0,i.Z)(e,[{key:"getMaintenanceHelper",value:function(){return a.Z.get(c+"helper",{headers:{Authorization:(0,o.Z)()}})}},{key:"getMaintenance",value:function(e,t){var n={item_class:e,item_type:t};return a.Z.get(c,{headers:{Authorization:(0,o.Z)()},params:n})}},{key:"postMaintenance",value:function(e){return a.Z.post(c,e,{headers:{Authorization:(0,o.Z)()}})}},{key:"putMaintenance",value:function(e){return a.Z.put(c,e,{headers:{Authorization:(0,o.Z)()}})}},{key:"getMaintenanceGp",value:function(e,t){var n={item_class:e,item_type:t};return a.Z.get(c+"gp",{headers:{Authorization:(0,o.Z)()},params:n})}},{key:"postMaintenanceGp",value:function(e){return a.Z.post(c+"gp",e,{headers:{Authorization:(0,o.Z)()}})}},{key:"putMaintenanceGp",value:function(e){return a.Z.put(c+"gp",e,{headers:{Authorization:(0,o.Z)()}})}},{key:"getMaintenanceActive",value:function(e,t,n){var r={item_class:e,item_type:t,gp:n};return a.Z.get(c+"active",{headers:{Authorization:(0,o.Z)()},params:r})}},{key:"postMaintenanceActive",value:function(e){return a.Z.post(c+"active",e,{headers:{Authorization:(0,o.Z)()}})}}]),e}();t.Z=new s},12248:function(e,t,n){n.r(t);var r=n(1413),i=n(74165),a=n(15861),o=n(29439),c=n(56890),s=n(35855),l=n(53994),u=n(53382),d=n(72791),h=n(23821),f=n(91933),m=n(59909),v=n(95907),p=n(16149),y=(n(93650),n(2423),n(87684)),x=n(80184),g={name:"",freq:"",freq_in_loc:"",enable:!1,requires:!1};t.default=function(){var e=(0,d.useState)(),t=(0,o.Z)(e,2),n=t[0],j=t[1],Z=(0,d.useState)(),w=(0,o.Z)(Z,2),N=w[0],b=w[1],k=(0,d.useState)(!1),_=(0,o.Z)(k,2),L=_[0],E=_[1],C=(0,d.useState)(g),S=(0,o.Z)(C,2),G=S[0],M=S[1],q=(0,f.useQuery)(["active-item-classes-with-item-type"],(0,a.Z)((0,i.Z)().mark((function e(){var t;return(0,i.Z)().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,y.Z.getMaintenanceHelper();case 2:return t=e.sent,e.abrupt("return",t.data);case 4:case"end":return e.stop()}}),e)}))),{onSuccess:function(e){j(e[0]),b(e[0].item_type[0])}}),A=q.data,z=q.isLoading,I=(0,f.useQuery)(["get-maintenances",null===N||void 0===N?void 0:N.id,null===n||void 0===n?void 0:n.item_class.id],(0,a.Z)((0,i.Z)().mark((function e(){var t;return(0,i.Z)().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,y.Z.getMaintenance(null===n||void 0===n?void 0:n.item_class.id,null===N||void 0===N?void 0:N.id);case 2:return t=e.sent,e.abrupt("return",t.data);case 4:case"end":return e.stop()}}),e)}))),{enabled:!1}),O=I.data,P=I.isLoading,F=I.refetch;(0,d.useEffect)((function(){N&&n&&F()}),[N]);var T=function(){var e=(0,a.Z)((0,i.Z)().mark((function e(){var t;return(0,i.Z)().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return t=(0,r.Z)((0,r.Z)({},G),{},{item_type:null===N||void 0===N?void 0:N.id,item_class:null===n||void 0===n?void 0:n.item_class.id}),e.next=3,t.id;case 3:if(!e.sent){e.next=7;break}e.t0=y.Z.putMaintenance(t),e.next=8;break;case 7:e.t0=y.Z.postMaintenance(t);case 8:e.t0,F(),M(g),E(!1);case 12:case"end":return e.stop()}}),e)})));return function(){return e.apply(this,arguments)}}();return z||P?(0,x.jsx)(m.Z,{}):(0,x.jsxs)("div",{children:[(0,x.jsx)("h3",{className:"page-title mb-3",children:"Maintenance Service"}),(0,x.jsx)("div",{className:"mt-3",children:(0,x.jsx)("div",{className:"card",children:(0,x.jsx)("div",{className:"card-body",children:(0,x.jsxs)("div",{className:"row",children:[(0,x.jsx)("div",{className:"col-sm-12 col-lg-6",children:(0,x.jsxs)(p.Z.Group,{className:"row",children:[(0,x.jsx)("label",{className:"col-sm-12",children:"Item class"}),(0,x.jsx)("div",{className:"col-sm-12",children:(0,x.jsx)(p.Z.Control,{onChange:function(e){var t;console.log(),j(A[e.target.value]),b(null===(t=A[e.target.value].item_type)||void 0===t?void 0:t[0])},className:"form-select",as:"select",children:A.map((function(e,t){return(0,x.jsx)("option",{value:t,children:e.item_class.title})}))})})]})}),(0,x.jsx)("div",{className:"col-sm-12 col-lg-6",children:(0,x.jsxs)(p.Z.Group,{className:"row",children:[(0,x.jsx)("label",{className:"col-sm-12",children:"item type"}),(0,x.jsx)("div",{className:"col-sm-12",children:(0,x.jsx)(p.Z.Control,{onChange:function(e){b(n.item_type[e.target.value])},className:"form-select",disabled:null===n,as:"select",children:null===n||void 0===n?void 0:n.item_type.map((function(e,t){return(0,x.jsx)("option",{value:t,children:e.title})}))})})]})})]})})})}),(0,x.jsx)("div",{className:"mt-3",children:(0,x.jsx)("div",{className:"card",children:(0,x.jsxs)("div",{className:"card-body",children:[(0,x.jsx)("h3",{className:"page-title mb-3",children:L?"Edit Maintenance Service":"New Maintenance Service"}),(0,x.jsxs)(p.Z.Group,{className:"row",children:[(0,x.jsx)("label",{className:"col-sm-4",style:{display:"flex",justifyContent:"flex-start",alignItems:"center"},children:"Service/ Maintenance items"}),(0,x.jsx)("div",{className:"col-sm-8",children:(0,x.jsx)(p.Z.Control,{onChange:function(e){e.persist(),M((function(t){return(0,r.Z)((0,r.Z)({},t),{},{name:e.target.value})}))},className:"form-control",value:null===G||void 0===G?void 0:G.name})})]}),(0,x.jsxs)(p.Z.Group,{className:"row",children:[(0,x.jsx)("label",{className:"col-sm-4",style:{display:"flex",justifyContent:"flex-start",alignItems:"center"},children:"Service Interval (day)"}),(0,x.jsx)("div",{className:"col-sm-8",children:(0,x.jsx)(p.Z.Control,{type:"number",min:"0",onChange:function(e){e.persist(),M((function(t){return(0,r.Z)((0,r.Z)({},t),{},{freq:e.target.value})}))},className:"form-control",value:null===G||void 0===G?void 0:G.freq})})]}),(0,x.jsxs)(p.Z.Group,{className:"row",children:[(0,x.jsx)("label",{className:"col-sm-4",style:{display:"flex",justifyContent:"flex-start",alignItems:"center"},children:"Interval per location"}),(0,x.jsx)("div",{className:"col-sm-8",children:(0,x.jsx)(p.Z.Control,{type:"number",min:1,onChange:function(e){e.persist(),M((function(t){return(0,r.Z)((0,r.Z)({},t),{},{freq_in_loc:e.target.value})}))},className:"form-control",value:null===G||void 0===G?void 0:G.freq_in_loc})})]}),(0,x.jsxs)(p.Z.Group,{className:"row",children:[(0,x.jsx)("label",{className:"col-sm-4",style:{display:"flex",justifyContent:"flex-start",alignItems:"center"},children:"Enable"}),(0,x.jsx)("div",{className:"col-sm-8",children:(0,x.jsx)("input",{type:"checkbox",checked:null===G||void 0===G?void 0:G.enable,onChange:function(e){e.persist(),M((function(t){return(0,r.Z)((0,r.Z)({},t),{},{enable:e.target.checked})}))}})})]}),(0,x.jsxs)(p.Z.Group,{className:"row",children:[(0,x.jsx)("label",{className:"col-sm-4",style:{display:"flex",justifyContent:"flex-start",alignItems:"center"},children:"Required"}),(0,x.jsx)("div",{className:"col-sm-8",children:(0,x.jsx)("input",{type:"checkbox",checked:null===G||void 0===G?void 0:G.requires,onChange:function(e){e.persist(),M((function(t){return(0,r.Z)((0,r.Z)({},t),{},{requires:e.target.checked})}))}})})]}),(0,x.jsxs)("div",{className:"row",children:[(0,x.jsx)("div",{className:"col-sm-1",children:(0,x.jsx)("button",{disabled:G===g,className:"btn btn-primary",onClick:T,children:"Accept"})}),(0,x.jsx)("div",{className:"col-sm-1",children:(0,x.jsx)("button",{className:"btn btn-secondary",onClick:function(){M(g),E(!1)},children:"Return"})})]})]})})}),(0,x.jsx)("div",{className:"mt-3",children:(0,x.jsx)("div",{className:"card",children:(0,x.jsx)("div",{className:"card-body p-3",children:(0,x.jsx)("div",{className:"row",children:(0,x.jsx)("div",{className:"mt-5 table-container",children:(0,x.jsxs)(h.Z,{children:[(0,x.jsx)(c.Z,{children:(0,x.jsxs)(s.Z,{children:[(0,x.jsx)(l.Z,{className:"col-sm-5",children:"Service/ Maintenance items"}),(0,x.jsx)(l.Z,{className:"col-sm-2",children:"Service Interval (day)"}),(0,x.jsx)(l.Z,{className:"col-sm-2",children:"Interval per location"}),(0,x.jsx)(l.Z,{className:"col-sm-1",children:"Enable"}),(0,x.jsx)(l.Z,{className:"col-sm-1",children:"Required"}),(0,x.jsx)(l.Z,{className:"col-sm-1",children:"Edit"})]})}),(0,x.jsx)(u.Z,{children:null===O||void 0===O?void 0:O.map((function(e){return(0,x.jsxs)(s.Z,{children:[(0,x.jsx)(l.Z,{className:"col-sm-5",children:e.name}),(0,x.jsx)(l.Z,{className:"col-sm-2",children:e.freq}),(0,x.jsx)(l.Z,{className:"col-sm-2",children:e.freq_in_loc}),(0,x.jsx)(l.Z,{className:"col-sm-1",children:(0,x.jsx)("input",{type:"checkbox",disabled:!0,checked:e.enable})}),(0,x.jsx)(l.Z,{className:"col-sm-1",children:(0,x.jsx)("input",{type:"checkbox",disabled:!0,checked:e.requires})}),(0,x.jsx)(l.Z,{className:"col-sm-2",children:(0,x.jsx)("button",{type:"button",className:"edit-btn",onClick:function(){M(e),E(!0)},children:(0,x.jsx)(v.Z,{})})})]},e.id)}))})]})})})})})})]})}},95907:function(e,t,n){var r=n(80184);t.Z=function(){return(0,r.jsx)(r.Fragment,{children:(0,r.jsx)("svg",{version:"1.1",xmlns:"http://www.w3.org/2000/svg",viewBox:"0 0 512 512",width:"20",height:"20",xmlnsXlink:"http://www.w3.org/1999/xlink","enable-background":"new 0 0 512 512",children:(0,r.jsx)("path",{d:"m455.1,137.9l-32.4,32.4-81-81.1 32.4-32.4c6.6-6.6 18.1-6.6 24.7,0l56.3,56.4c6.8,6.8 6.8,17.9 0,24.7zm-270.7,271l-81-81.1 209.4-209.7 81,81.1-209.4,209.7zm-99.7-42l60.6,60.7-84.4,23.8 23.8-84.5zm399.3-282.6l-56.3-56.4c-11-11-50.7-31.8-82.4,0l-285.3,285.5c-2.5,2.5-4.3,5.5-5.2,8.9l-43,153.1c-2,7.1 0.1,14.7 5.2,20 5.2,5.3 15.6,6.2 20,5.2l153-43.1c3.4-0.9 6.4-2.7 8.9-5.2l285.1-285.5c22.7-22.7 22.7-59.7 0-82.5z"})})})}},23821:function(e,t,n){var r=n(39281),i=n(79836),a=n(80184);t.Z=function(e){var t=e.children;return(0,a.jsx)(a.Fragment,{children:(0,a.jsx)(r.Z,{children:(0,a.jsx)(i.Z,{children:t})})})}},93650:function(){},15861:function(e,t,n){function r(e,t,n,r,i,a,o){try{var c=e[a](o),s=c.value}catch(l){return void n(l)}c.done?t(s):Promise.resolve(s).then(r,i)}function i(e){return function(){var t=this,n=arguments;return new Promise((function(i,a){var o=e.apply(t,n);function c(e){r(o,i,a,c,s,"next",e)}function s(e){r(o,i,a,c,s,"throw",e)}c(void 0)}))}}n.d(t,{Z:function(){return i}})},74165:function(e,t,n){n.d(t,{Z:function(){return i}});var r=n(71002);function i(){i=function(){return e};var e={},t=Object.prototype,n=t.hasOwnProperty,a="function"==typeof Symbol?Symbol:{},o=a.iterator||"@@iterator",c=a.asyncIterator||"@@asyncIterator",s=a.toStringTag||"@@toStringTag";function l(e,t,n){return Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}),e[t]}try{l({},"")}catch(E){l=function(e,t,n){return e[t]=n}}function u(e,t,n,r){var i=t&&t.prototype instanceof f?t:f,a=Object.create(i.prototype),o=new k(r||[]);return a._invoke=function(e,t,n){var r="suspendedStart";return function(i,a){if("executing"===r)throw new Error("Generator is already running");if("completed"===r){if("throw"===i)throw a;return L()}for(n.method=i,n.arg=a;;){var o=n.delegate;if(o){var c=w(o,n);if(c){if(c===h)continue;return c}}if("next"===n.method)n.sent=n._sent=n.arg;else if("throw"===n.method){if("suspendedStart"===r)throw r="completed",n.arg;n.dispatchException(n.arg)}else"return"===n.method&&n.abrupt("return",n.arg);r="executing";var s=d(e,t,n);if("normal"===s.type){if(r=n.done?"completed":"suspendedYield",s.arg===h)continue;return{value:s.arg,done:n.done}}"throw"===s.type&&(r="completed",n.method="throw",n.arg=s.arg)}}}(e,n,o),a}function d(e,t,n){try{return{type:"normal",arg:e.call(t,n)}}catch(E){return{type:"throw",arg:E}}}e.wrap=u;var h={};function f(){}function m(){}function v(){}var p={};l(p,o,(function(){return this}));var y=Object.getPrototypeOf,x=y&&y(y(_([])));x&&x!==t&&n.call(x,o)&&(p=x);var g=v.prototype=f.prototype=Object.create(p);function j(e){["next","throw","return"].forEach((function(t){l(e,t,(function(e){return this._invoke(t,e)}))}))}function Z(e,t){function i(a,o,c,s){var l=d(e[a],e,o);if("throw"!==l.type){var u=l.arg,h=u.value;return h&&"object"==(0,r.Z)(h)&&n.call(h,"__await")?t.resolve(h.__await).then((function(e){i("next",e,c,s)}),(function(e){i("throw",e,c,s)})):t.resolve(h).then((function(e){u.value=e,c(u)}),(function(e){return i("throw",e,c,s)}))}s(l.arg)}var a;this._invoke=function(e,n){function r(){return new t((function(t,r){i(e,n,t,r)}))}return a=a?a.then(r,r):r()}}function w(e,t){var n=e.iterator[t.method];if(void 0===n){if(t.delegate=null,"throw"===t.method){if(e.iterator.return&&(t.method="return",t.arg=void 0,w(e,t),"throw"===t.method))return h;t.method="throw",t.arg=new TypeError("The iterator does not provide a 'throw' method")}return h}var r=d(n,e.iterator,t.arg);if("throw"===r.type)return t.method="throw",t.arg=r.arg,t.delegate=null,h;var i=r.arg;return i?i.done?(t[e.resultName]=i.value,t.next=e.nextLoc,"return"!==t.method&&(t.method="next",t.arg=void 0),t.delegate=null,h):i:(t.method="throw",t.arg=new TypeError("iterator result is not an object"),t.delegate=null,h)}function N(e){var t={tryLoc:e[0]};1 in e&&(t.catchLoc=e[1]),2 in e&&(t.finallyLoc=e[2],t.afterLoc=e[3]),this.tryEntries.push(t)}function b(e){var t=e.completion||{};t.type="normal",delete t.arg,e.completion=t}function k(e){this.tryEntries=[{tryLoc:"root"}],e.forEach(N,this),this.reset(!0)}function _(e){if(e){var t=e[o];if(t)return t.call(e);if("function"==typeof e.next)return e;if(!isNaN(e.length)){var r=-1,i=function t(){for(;++r<e.length;)if(n.call(e,r))return t.value=e[r],t.done=!1,t;return t.value=void 0,t.done=!0,t};return i.next=i}}return{next:L}}function L(){return{value:void 0,done:!0}}return m.prototype=v,l(g,"constructor",v),l(v,"constructor",m),m.displayName=l(v,s,"GeneratorFunction"),e.isGeneratorFunction=function(e){var t="function"==typeof e&&e.constructor;return!!t&&(t===m||"GeneratorFunction"===(t.displayName||t.name))},e.mark=function(e){return Object.setPrototypeOf?Object.setPrototypeOf(e,v):(e.__proto__=v,l(e,s,"GeneratorFunction")),e.prototype=Object.create(g),e},e.awrap=function(e){return{__await:e}},j(Z.prototype),l(Z.prototype,c,(function(){return this})),e.AsyncIterator=Z,e.async=function(t,n,r,i,a){void 0===a&&(a=Promise);var o=new Z(u(t,n,r,i),a);return e.isGeneratorFunction(n)?o:o.next().then((function(e){return e.done?e.value:o.next()}))},j(g),l(g,s,"Generator"),l(g,o,(function(){return this})),l(g,"toString",(function(){return"[object Generator]"})),e.keys=function(e){var t=[];for(var n in e)t.push(n);return t.reverse(),function n(){for(;t.length;){var r=t.pop();if(r in e)return n.value=r,n.done=!1,n}return n.done=!0,n}},e.values=_,k.prototype={constructor:k,reset:function(e){if(this.prev=0,this.next=0,this.sent=this._sent=void 0,this.done=!1,this.delegate=null,this.method="next",this.arg=void 0,this.tryEntries.forEach(b),!e)for(var t in this)"t"===t.charAt(0)&&n.call(this,t)&&!isNaN(+t.slice(1))&&(this[t]=void 0)},stop:function(){this.done=!0;var e=this.tryEntries[0].completion;if("throw"===e.type)throw e.arg;return this.rval},dispatchException:function(e){if(this.done)throw e;var t=this;function r(n,r){return o.type="throw",o.arg=e,t.next=n,r&&(t.method="next",t.arg=void 0),!!r}for(var i=this.tryEntries.length-1;i>=0;--i){var a=this.tryEntries[i],o=a.completion;if("root"===a.tryLoc)return r("end");if(a.tryLoc<=this.prev){var c=n.call(a,"catchLoc"),s=n.call(a,"finallyLoc");if(c&&s){if(this.prev<a.catchLoc)return r(a.catchLoc,!0);if(this.prev<a.finallyLoc)return r(a.finallyLoc)}else if(c){if(this.prev<a.catchLoc)return r(a.catchLoc,!0)}else{if(!s)throw new Error("try statement without catch or finally");if(this.prev<a.finallyLoc)return r(a.finallyLoc)}}}},abrupt:function(e,t){for(var r=this.tryEntries.length-1;r>=0;--r){var i=this.tryEntries[r];if(i.tryLoc<=this.prev&&n.call(i,"finallyLoc")&&this.prev<i.finallyLoc){var a=i;break}}a&&("break"===e||"continue"===e)&&a.tryLoc<=t&&t<=a.finallyLoc&&(a=null);var o=a?a.completion:{};return o.type=e,o.arg=t,a?(this.method="next",this.next=a.finallyLoc,h):this.complete(o)},complete:function(e,t){if("throw"===e.type)throw e.arg;return"break"===e.type||"continue"===e.type?this.next=e.arg:"return"===e.type?(this.rval=this.arg=e.arg,this.method="return",this.next="end"):"normal"===e.type&&t&&(this.next=t),h},finish:function(e){for(var t=this.tryEntries.length-1;t>=0;--t){var n=this.tryEntries[t];if(n.finallyLoc===e)return this.complete(n.completion,n.afterLoc),b(n),h}},catch:function(e){for(var t=this.tryEntries.length-1;t>=0;--t){var n=this.tryEntries[t];if(n.tryLoc===e){var r=n.completion;if("throw"===r.type){var i=r.arg;b(n)}return i}}throw new Error("illegal catch attempt")},delegateYield:function(e,t,n){return this.delegate={iterator:_(e),resultName:t,nextLoc:n},"next"===this.method&&(this.arg=void 0),h}},e}}}]);
//# sourceMappingURL=2248.1b780e7a.chunk.js.fd59eab3b84c.map