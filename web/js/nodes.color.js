// import { app } from "../../../scripts/app.js";
// import { $el } from "../../../scripts/ui.js";
// import { get_rgba,isColorBright } from "./util.color.js";
// console.log(app)

// function COLOR_RGBA(key, [r,g,b,a]) {
//     const widget = {}
//     widget.x = 0
//     widget.y = 0
//     widget.name = key
//     widget.type = 'COLOR_RGBA'
//     widget.options = { default: '#FF0000'}
//     widget.value = [r,g,b,a]
    
//     widget.draw = function (ctx, node, widgetWidth, widgetY, height) {
//         const hide = this.type !== 'COLOR_RGBA' && app.canvas.ds.scale > 0.5
//         if (hide) {
//             return
//         }
//         const border = 3
//         ctx.fillStyle = '#000'
//         ctx.fillRect(0, widgetY, widgetWidth, height)

//         ctx.fillStyle = toRgba()
//         ctx.fillRect(
//             border,
//             widgetY + border,
//             widgetWidth - border * 2,
//             height - border * 2,
//         )

//         ctx.fillStyle = isColorBright(color.values, 125) ? '#000' : '#fff'
//         ctx.font = '14px Arial'
//         ctx.textAlign = 'center'
//         ctx.fillText(this.name, widgetWidth * 0.5, widgetY + 14)

//     }

//     widget.mouse = function (e, pos, node) {
//         if (e.type === 'pointerdown') {
//           const widgets = node.widgets.filter((w) => w.type === 'COLOR')
  
//           for (const w of widgets) {
//             // color picker
//             const rect = [w.last_y, w.last_y + 32]
//             if (pos[1] > rect[0] && pos[1] < rect[1]) {
//               const picker = document.createElement('input')
//               picker.type = 'color'
//               picker.value = this.value
  
//               picker.style.position = 'absolute'
//               picker.style.left = '999999px' //(window.innerWidth / 2) + "px";
//               picker.style.top = '999999px' //(window.innerHeight / 2) + "px";
  
//               document.body.appendChild(picker)
  
//               picker.addEventListener('change', () => {
//                 this.value = picker.value
//                 this.callback?.(this.value)
//                 node.graph._version++
//                 node.setDirtyCanvas(true, true)
//                 picker.remove()
//               })
  
//               picker.click()
//             }
//           }
//         }
//       }
//     widget.computeSize = function (width) {
//       return [width, 32]
//     }
//     return widget;
// }

// app.registerExtension({
//     name: "Ryota.widgets",
//     getCustomWidgets(app) {
//         return {
//             "COLOR:RGBA": (node, inputName, inputData, _app) => {
//                 console.log(node, inputName, inputData, _app, app)

//                 const color = get_rgba(inputData[1]?.default || "#FFFFFFFF");
                
//                 console.log(node.pos, color)
                
//                 return {
//                     widget: node.addCustomWidget(COLOR_RGBA(inputName, color)),
//                     minWidth: 150,
//                     minHeight: 30,
//                 }
//             }
//             // COLOR_RGBA(node, inputName, inputData, _app) {
//             //     console.log(app, node, inputName, inputData, _app)
//             //     return {
//             //         widget: node.addCustomWidget(
//             //             COLOR_RGBA(0, 0, inputName, inputData[1]?.default || '#FFFFFFFF'),
//             //         ),
//             //         minWidth: 150,
//             //         minHeight: 30,
//             //     }
//             // }

//         }
//     }
// });
