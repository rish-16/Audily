document.addEventListener("DOMContentLoaded", () => {
    const imgPicker = document.getElementById('img-picker')
    const submitBtn = document.getElementById('submit')
    
    submitBtn.addEventListener("click", () => {
        
    })
    
    imgPicker.addEventListener("change",  handleFiles, false)
    
    function handleFiles() {
        const fileList = this.files
        
        const numFiles = fileList.length
        console.log(numFiles)
        
        for (let i = 0; i < numFiles; i++) {
            const file = fileList[i]
            
            document.body.innerHTML += `<p>${file.name}</p>`
            
            var canvas = document.createElement("canvas")
            var ctx = canvas.getContext('2d')
            
            var img = new Image()
            
            img.onload = function() {
                ctx.drawImage(img, 0, 0)
                var base64 = canvas.toDataURL()
                
                // send to backend
                console.log("Sending image to API")
                $.post(
                    'http://localhost:5000/audily',
                    base64,
                    function (data, status, info) {
                        console.log(data)
                    }
                )   
            }
            
            img.src = URL.createObjectURL(file);
        }
    }
})