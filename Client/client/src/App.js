import React, { useState } from 'react';
import axios from 'axios';
import Loading from './Components/Loading';
const App = () => {
  const [output, setOutput] = useState("");
  const [loding, setLoding] = useState(false);
  const [dispImage, setDispImage] = useState();
  const [image, setImage] = useState("");

  const inputStyle = {
    opacity:"0",
    width: "0.1px",
    height: "0.1px",
    position: "absolute",
    backgroundColor: "#7873f5",
  }

  const handleClick = async ()=>{
    setOutput("");
    setLoding(true);
    const formData = new FormData();
    formData.append("image", image);
    console.log(formData.get("image"));

    try{
       await axios.post("http://localhost:5000/home", formData).then(response=>{setOutput(response.data.message); setLoding(false)});
    }
    catch(error){
      console.log("Request error");
    }
  }

  const imageSelected = (event)=>{
      setImage(event.target.files[0]);
      var reader = new FileReader();
      reader.readAsDataURL(event.target.files[0]);
      reader.onload = ()=>{
          setDispImage(reader.result);
        }
    }

  return (
    <div>
      <h1>ImageSense</h1>
      <div className="input-window">
        <img src={dispImage} height={100} width={100} className='img'/>

        <div className="file-input ">
          <input type="file" accept="image/*" onChange={imageSelected} id="file" className="file" style={inputStyle}/>
          <label for="file">
            Select file
          <p className="file-name"></p>
          </label>
          <button onClick={handleClick} className="btn-hover color-1">Submit</button>

        </div>

      </div>
      <div class="output">
        <p class="output-heading">Output : </p>
        <p class="output-txt">{loding? <Loading/>: output}</p>
      </div>

    </div>
  )
}

export default App
