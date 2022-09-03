"use strict";(self.webpackChunkinventory=self.webpackChunkinventory||[]).push([[2963],{32963:function(e,s,n){n.r(s),n.d(s,{default:function(){return F}});var a=n(1413),t=n(15671),o=n(43144),r=n(97326),l=n(60136),i=n(54062),c=n(72791),u=n(79271),d=n(16149),m=n(60364),h=n(48858),f=(n(8859),n(87462)),p=n(63366),v=n(81694),b=n.n(v),g=n(55746),x=n(91683),w=Math.pow(2,31)-1;function y(e,s,n){var a=n-Date.now();e.current=a<=w?setTimeout(s,a):setTimeout((function(){return y(e,s,n)}),w)}function N(){var e=(0,g.Z)(),s=(0,c.useRef)();return(0,x.Z)((function(){return clearTimeout(s.current)})),(0,c.useMemo)((function(){var n=function(){return clearTimeout(s.current)};return{set:function(a,t){void 0===t&&(t=0),e()&&(n(),t<=w?s.current=setTimeout(a,t):y(s,a,Date.now()+t))},clear:n}}),[])}var C=n(72709),Z=n(52134),k=n(10162),j=n(80473),E=c.createContext({onClose:function(){}}),P=["bsPrefix","closeLabel","closeButton","className","children"],L=c.forwardRef((function(e,s){var n=e.bsPrefix,a=e.closeLabel,t=e.closeButton,o=e.className,r=e.children,l=(0,p.Z)(e,P);n=(0,k.vE)(n,"toast-header");var i=(0,c.useContext)(E),u=(0,Z.Z)((function(e){i&&i.onClose&&i.onClose(e)}));return c.createElement("div",(0,f.Z)({ref:s},l,{className:b()(n,o)}),r,t&&c.createElement(j.Z,{label:a,onClick:u,className:"ml-2 mb-1","data-dismiss":"toast"}))}));L.displayName="ToastHeader",L.defaultProps={closeLabel:"Close",closeButton:!0};var S=L,R=(0,n(66543).Z)("toast-body"),T=["bsPrefix","className","children","transition","show","animation","delay","autohide","onClose"],q=c.forwardRef((function(e,s){var n=e.bsPrefix,a=e.className,t=e.children,o=e.transition,r=void 0===o?C.Z:o,l=e.show,i=void 0===l||l,u=e.animation,d=void 0===u||u,m=e.delay,h=void 0===m?3e3:m,v=e.autohide,g=void 0!==v&&v,x=e.onClose,w=(0,p.Z)(e,T);n=(0,k.vE)(n,"toast");var y=(0,c.useRef)(h),Z=(0,c.useRef)(x);(0,c.useEffect)((function(){y.current=h,Z.current=x}),[h,x]);var j=N(),P=!(!g||!i),L=(0,c.useCallback)((function(){P&&(null==Z.current||Z.current())}),[P]);(0,c.useEffect)((function(){j.set(L,y.current)}),[j,L]);var S=(0,c.useMemo)((function(){return{onClose:x}}),[x]),R=!(!r||!d),q=c.createElement("div",(0,f.Z)({},w,{ref:s,className:b()(n,a,!R&&(i?"show":"hide")),role:"alert","aria-live":"assertive","aria-atomic":"true"}),t);return c.createElement(E.Provider,{value:S},R&&r?c.createElement(r,{in:i,unmountOnExit:!0},q):q)}));q.displayName="Toast";var D=Object.assign(q,{Body:R,Header:S}),B=n(80184),U=function(e){(0,l.Z)(n,e);var s=(0,i.Z)(n);function n(e){var o;return(0,t.Z)(this,n),(o=s.call(this,e)).handleClosesnack=function(e,s){"clickaway"!==s&&o.setState({snackopen:!1})},o.handleClickShowPassword=function(){o.setState({values:(0,a.Z)((0,a.Z)({},o.state.values),{},{showPassword:!o.state.values.showPassword})})},o.handleLogin=o.handleLogin.bind((0,r.Z)(o)),o.onChangeUsername=o.onChangeUsername.bind((0,r.Z)(o)),o.onChangePassword=o.onChangePassword.bind((0,r.Z)(o)),o.handleClickShowPassword=o.handleClickShowPassword.bind((0,r.Z)(o)),o.alerthandle=o.alerthandle.bind((0,r.Z)(o)),o.state={username:"",password:"",content:"",loading:!1,name:"",values:{showPassword:!1},snackopen:!1,loadfile:!1,type:"success",progress:0,source:null,open:!1},o}return(0,o.Z)(n,[{key:"alerthandle",value:function(e,s){this.setState({content:e,type:s,snackopen:!0})}},{key:"onChangeUsername",value:function(e){console.log(e.target.value),this.setState({username:e.target.value,name:e.target.value})}},{key:"onChangePassword",value:function(e){this.setState({password:e.target.value})}},{key:"handleLogin",value:function(e){var s=this;if(e.preventDefault(),this.setState({loading:!0}),""==this.state.username)return this.alerthandle("Username is required","error"),void this.setState({loading:!1});if(""==this.state.password)return this.alerthandle("Password is required","alert"),void this.setState({loading:!1});var n=this.props,a=n.dispatch,t=n.history;a((0,h.x4)(this.state.username,this.state.password)).then((function(){s.alerthandle("Login Successful","success"),s.sleep(5e5),t.push("/dashboard"),window.location.reload()})).catch((function(){s.alerthandle("Login failed ","alert"),s.setState({loading:!1})}))}},{key:"handleMouseDownPassword",value:function(e){e.preventDefault()}},{key:"render",value:function(){var e=this,s=this.props,n=s.isLoggedIn;s.message;return console.log(n),n?(0,B.jsx)(u.l_,{to:"/dashboard"}):(0,B.jsxs)("section",{className:"background-radial-gradient overflow-hidden",children:[(0,B.jsx)("div",{className:"container px-4 py-5 px-md-5 text-center text-lg-start my-5",children:(0,B.jsxs)("div",{className:"row gx-lg-5 align-items-center mb-5",children:[(0,B.jsxs)("div",{className:"col-lg-6 mb-5 mb-lg-0",style:{Zindex:"10"},children:[(0,B.jsxs)("h1",{className:"my-5 display-5 fw-bold ls-tight",style:{color:"hsl(218, 81%, 95%)"},children:["Inventory  ",(0,B.jsx)("br",{}),(0,B.jsx)("span",{style:{color:"hsl(218, 81%, 75%)"},children:"and Gap analyses system"})]}),(0,B.jsx)("p",{className:"mb-5 opacity-70 mt-5",style:{color:"hsl(218, 81%, 85%)"},children:"Lorem ipsum dolor, sit amet consectetur adipisicing elit. Temporibus, expedita iusto veniam atque, magni tempora mollitia dolorum consequatur nulla, neque debitis eos reprehenderit quasi ab ipsum nisi dolorem modi. Quos?"})]}),(0,B.jsxs)("div",{className:"offset-1 col-lg-4 mb-5 mb-lg-0 position-relative mt-5",children:[(0,B.jsx)("div",{id:"radius-shape-1",className:"position-absolute rounded-circle shadow-5-strong"}),(0,B.jsx)("div",{id:"radius-shape-2",className:"position-absolute shadow-5-strong"}),(0,B.jsx)("div",{className:"card bg-glass  mb-5 mt-5",children:(0,B.jsx)("div",{className:"card-body px-5 py-5 px-md-5 col-md-12",children:(0,B.jsxs)(d.Z,{onSubmit:this.handleLogin,ref:function(s){e.form=s},children:[(0,B.jsxs)("div",{className:"form-outline mb-4 mt-2",children:[(0,B.jsx)("label",{className:"form-label",htmlFor:"form3Example3",children:"Username"}),(0,B.jsx)("input",{onChange:function(s){e.onChangeUsername(s)},type:"text",id:"form3Example3",className:"form-control"})]}),(0,B.jsxs)("div",{className:"form-outline mb-4",children:[(0,B.jsx)("label",{className:"form-label",htmlFor:"form3Example4",children:"Password"}),(0,B.jsx)("input",{onChange:function(s){e.onChangePassword(s)},type:"password",id:"form3Example4",className:"form-control"})]}),(0,B.jsx)("div",{className:"form-check d-flex justify-content-center mb-4"}),(0,B.jsxs)("button",{type:"submit",className:"btn btn-primary btn-block mb-4",children:["sign in",this.state.loading&&(0,B.jsx)("span",{className:"mr-2 pr-1 pl-2 spinner-border spinner-border-sm"})]})]})})})]})]})}),(0,B.jsx)(D,{style:{position:"absolute",top:"90vh",right:"18vw",backgroundColor:"success"==this.state.type?"hsl(218, 81%, 95%)":"#F8D7DA",color:"#000"},onClose:function(s){e.handleClosesnack(s)},show:this.state.snackopen,delay:3e3,autohide:!0,className:"d-inline-block m-1",bg:this.state.type,children:(0,B.jsx)(D.Body,{children:this.state.content})})]})}}]),n}(c.Component);var F=(0,m.$j)((function(e){return{isLoggedIn:e.auth.isLoggedIn,message:e.message.message}}))(U)},91683:function(e,s,n){n.d(s,{Z:function(){return t}});var a=n(72791);function t(e){var s=function(e){var s=(0,a.useRef)(e);return s.current=e,s}(e);(0,a.useEffect)((function(){return function(){return s.current()}}),[])}},80473:function(e,s,n){var a=n(87462),t=n(63366),o=n(52007),r=n.n(o),l=n(72791),i=n(81694),c=n.n(i),u=["label","onClick","className"],d={label:r().string.isRequired,onClick:r().func},m=l.forwardRef((function(e,s){var n=e.label,o=e.onClick,r=e.className,i=(0,t.Z)(e,u);return l.createElement("button",(0,a.Z)({ref:s,type:"button",className:c()("close",r),onClick:o},i),l.createElement("span",{"aria-hidden":"true"},"\xd7"),l.createElement("span",{className:"sr-only"},n))}));m.displayName="CloseButton",m.propTypes=d,m.defaultProps={label:"Close"},s.Z=m},72709:function(e,s,n){var a,t=n(87462),o=n(63366),r=n(81694),l=n.n(r),i=n(72791),c=n(26752),u=n(71380),d=n(67202),m=["className","children"],h=((a={})[c.d0]="show",a[c.cn]="show",a),f=i.forwardRef((function(e,s){var n=e.className,a=e.children,r=(0,o.Z)(e,m),f=(0,i.useCallback)((function(e){(0,d.Z)(e),r.onEnter&&r.onEnter(e)}),[r]);return i.createElement(c.ZP,(0,t.Z)({ref:s,addEndListener:u.Z},r,{onEnter:f}),(function(e,s){return i.cloneElement(a,(0,t.Z)({},s,{className:l()("fade",n,a.props.className,h[e])}))}))}));f.defaultProps={in:!1,timeout:300,mountOnEnter:!1,unmountOnExit:!1,appear:!1},f.displayName="Fade",s.Z=f}}]);
//# sourceMappingURL=2963.19de7586.chunk.js.map