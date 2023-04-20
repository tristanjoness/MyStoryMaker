<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Story Generator</title>
  </head>
  <body>
    <h1>Story Generator</h1>
    <p>Click the button to generate a random story:</p>
    <button onclick="generateStory()">Generate Story</button>
    <p id="story"></p>

    <script>
      function generateStory() {
        // Define arrays of story elements
        var characters = ['princess', 'pirate', 'wizard', 'robot', 'alien'];
        var settings = ['castle', 'space station', 'underwater cave', 'forest', 'haunted house'];
        var conflicts = ['fighting a dragon', 'finding a treasure', 'rescuing a friend', 'escaping a monster', 'solving a mystery'];
      
        // Select a random element from each array
        var character = characters[Math.floor(Math.random() * characters.length)];
        var setting = settings[Math.floor(Math.random() * settings.length)];
        var conflict = conflicts[Math.floor(Math.random() * conflicts.length)];
      
        // Build the story text
        var story = "Once upon a time, there was a " + character + " who found themselves in a " + setting + ". They were faced with the challenge of " + conflict + ".";
      
        // Display the story on the page
        document.getElementById("story").innerHTML = story;
      }
    </script>
  </body>
</html>
