// function _h2i(s, x) {
//     return parseInt(s.slice(x*2+1, x*2+3, 16))
// }

// function _i2h(n) {
//     const v = Number(n).toString(16)
//     if(v.length <2)
//         return `0${v}`
//     return v
// }

// export function get(hex, mode='RGB') {
//     if (mode ==='RGBA') {
//         return getRgba(hex)
//     }
//     if (mode === 'RGB') {
//         return getRgba(hex)
//     }
// }

// export function getRgb(hex) {
//     const regRgb = /^#[0-9A-F]{6}$/i
//     if(regRgb.test(hex)) {
//         return [_h2i(hex,0), _h2i(hex,1), _h2i(hex,2)]
//     }
//     return [0,0,0]
// }
// export function getRgba(hex) {
//     const regRgba = /^#[0-9A-F]{8}$/i
//     if(regRgba.test(hex)) {
//         return [_h2i(hex,0), _h2i(hex,1), _h2i(hex,2), _h2i(hex,3)]
//     }
//     return [0,0,0]
// }

// export function toRgba([r,g,b,a]) {
//     return `rgba(${_i2h(r),_i2h(g),_i2h(b),_i2h(a)})`;
// }

// export function getBrightness(rgbObj) {
//     return Math.round(
//       (Number.parseInt(rgbObj[0]) * 299 +
//         Number.parseInt(rgbObj[1]) * 587 +
//         Number.parseInt(rgbObj[2]) * 114) /
//         1000,
//     )
// }
// export function isColorBright (color, threshold=125) {

// }