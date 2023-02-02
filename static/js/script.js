// Function that does not allow the user to submit the form until a file is uploaded
document.addEventListener("DOMContentLoaded", disallowBlankForm);
function disallowBlankForm() {
   document.querySelector("#convert-button").addEventListener("click", function (event) {
   if (!document.getElementById("file").value) {
     event.preventDefault();
     alert("Please select a file");
     }
   })
};


// Function that displays converted file name in the download div after it's been converted
if(document.getElementById("download-container")) {
  var reloadContent = document.getElementById("download");
  var text = reloadContent.innerHTML;
  if (text.trim().length > 9) {
    //the string "Download" is 8 characters long trimmed
    document.getElementById("download-container").classList.remove("d-none");
  }
}


// Function that displays converted file name in the hidden div after it's been converted
if(document.getElementById("results-container")) {
  var reloadContent = document.getElementById("result");
  var text = reloadContent.innerHTML;
  if (text.trim().length > 0) {
    //the string "Download" is 8 characters long trimmed
    document.getElementById("results-container").classList.remove("d-none");
 }
};

// Function that hides the random 5 digits from the users display on the download button
document.addEventListener('DOMContentLoaded', () => {
  const downloadLink = document.getElementById('download');
  if (downloadLink) {
    const fileName = downloadLink.href.substring(downloadLink.href.lastIndexOf('/') + 1);
    const modifiedFileName = fileName.substring(5);
    downloadLink.textContent = `Download ${modifiedFileName}`;
  }
});


// Function that change the tooltip text after your cursor leaves the tooltip
document.addEventListener("DOMContentLoaded", function() {
  // Check if the "copy-icon" element exists on the page
  if(document.getElementById("copy-icon")) {
      document.getElementById("copy-icon").addEventListener("mouseleave", changeText);
      function changeText() {
          var copy_text = document.getElementById("tooltiptext");
          copy_text.innerHTML = "Copy text";
      }
  }
});


// Rotate the tips and tricks cheveron when it's clicked
document.querySelector(".tog").addEventListener("click", function() {
  const icon = document.querySelector(".chev");
  icon.classList.toggle("fa-chevron-down");
  icon.classList.toggle("fa-chevron-up");
  icon.style.transition = "transform 0.9s ease";
});

// Add an event listener and function that copies the result text and changes the tooltip text when copied
document.addEventListener("DOMContentLoaded", copyText);
function copyText() {
    // Check if the "copy-icon" element exists on the page
    if(document.getElementById("copy-icon")) {
        document.getElementById("copy-icon").addEventListener("click", copyMe);
        function copyMe() {
            // Copy the result text
            navigator.clipboard.writeText(document.getElementById("result").innerText);

            // Change the tooltip text to say copied after click
            var copy_text = document.getElementById("tooltiptext");
            copy_text.innerHTML = "Copied!";
        }
    }
};


//Drag and drop\
let dropArea = document.body;
    // let dragMessage = document.getElementById("drag-message");

    // Prevent default drag behaviors
    ["dragenter", "dragover", "dragleave", "drop"].forEach((eventName) => {
    dropArea.addEventListener(eventName, preventDefaults, false);
    document.body.addEventListener(eventName, preventDefaults, false);
    });

    // Highlight entire body when item is dragged over it
    ["dragenter", "dragover"].forEach((eventName) => {
    dropArea.addEventListener(eventName, highlight, false);
    });

    // Unhighlight entire body when item is removed from the drag area
    ["dragleave", "drop"].forEach((eventName) => {
    dropArea.addEventListener(eventName, unhighlight, false);
    });

    // Handle dropped files
    dropArea.addEventListener("drop", handleDrop, false);

    function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
    }

    function highlight(e) {
    dropArea.classList.add("hlight");
    // dragMessage.style.display = null;
    }

    function unhighlight(e) {
    dropArea.classList.remove("hlight");
    // dragMessage.style.display = 'none';
    }

    function checkFileValidity(input, file) {
      // Check that the file size is under 10MB
      if (file.size > 1024 * 1024 * 10) {
        // 10 MB
        input.value = "";
        alert("File is too large (max size is 10 MB).");
        return false;
      }
    
      // Check that the file title length is under 30 characters
      if (file.name.length > 30) {
        input.value = "";
        alert("File title is too long (max length is 30 characters).");
        return false;
      }
    
      // Check that the file extension is an acceptable format
      var extentionName = file.name.split(".").pop();
      var allowedExtensions;
      if (document.location.pathname === "/ocr") {
        allowedExtensions = ["jpeg", "jpg", "png", "tiff", "bmp"];
      } else {
        allowedExtensions = ["pdf"];
      }
      if (!allowedExtensions.includes(extentionName.toLowerCase())) {
        input.value = "";
        alert("Invalid file type");
        return false;
      }
      return true;
    }
    

    function updateProgressBar() {
    $("#progress-bar")
        .attr("aria-valuenow", 100 + "%")
        .css("width", 100 + "%");
    }

    function updateLabel(input, fileName) {
    var label = input.previousElementSibling;
    if (fileName) {
        label.innerHTML = fileName;
    } else {
        label.innerHTML = "Choose file";
    }
    }

    function handleBrowse() {
      const input = document.getElementById("file");
      const files = input.files;
    
      if (files.length > 0) {
        if (document.location.pathname === "/merge-pdf") {
          if (files.length > 1) {
            updateLabel(input, 'Multiple files selected');
          } else {
            updateLabel(input, 'Select more files');
          }
        } else {
          updateLabel(input, files[0].name);
        }
        for (let i = 0; i < files.length; i++) {
          const file = files[i];
          if (checkFileValidity(input, file)) {
            updateProgressBar();
            input.files = files;
          }
        }
      }
    }
    
    function handleDrop(e) {
      e.preventDefault();
      e.stopPropagation();
    
      const input = document.getElementById("file");
      const files = e.dataTransfer.files;
    
      if (files.length > 0) {
        if (document.location.pathname === "/merge-pdf") {
          if (files.length > 1) {
            updateLabel(input, 'Multiple files selected');
          } else {
            updateLabel(input, 'Select more files');
          }
        } else {
          updateLabel(input, files[0].name);
        }
        for (let i = 0; i < files.length; i++) {
          const file = files[i];
          if (checkFileValidity(input, file)) {
            updateProgressBar();
            input.files = files;
          }
        }
      }
    }
    
    
    
    