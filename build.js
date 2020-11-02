var fs = require('fs-extra')

fs.copySync('./build/Release', './bin')
fs.copyFileSync('./SimConnect SDK/lib/SimConnect.dll', './bin/SimConnect.dll')

console.log('Done.')