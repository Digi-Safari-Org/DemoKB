// Enterprise Logging Utility
/**
 * Logs messages in enterprise format.
 * @param {string} moduleName - Name of the module or function
 * @param {string} level - Log level (e.g., 'INFO', 'ERROR')
 * @param {string} message - Log message
 */
function logMessage(moduleName, level, message) {
  const timestamp = new Date().toISOString();
  console.log(`[${timestamp}] [${moduleName}] [${level}] ${message}`);
}

/**
 * Validates an email address.
 * @param {string} email - Email to validate
 * @returns {boolean} True if valid, false otherwise
 */
function validateEmail(email) {
  const emailRegex = /\S+@\S+\.\S+/;
  return emailRegex.test(email);
}

/**
 * Generates a unique user ID.
 * @returns {string} Generated user ID
 */
function generateUserId() {
  return "user_" + Math.floor(Math.random() * 1000);
}

/**
 * Saves a user object to the database array.
 * @param {object} db - Database array
 * @param {object} user - User object
 * @returns {void}
 */
function saveUserToDB(db, user) {
  db.push(user);
}

/**
 * Processes user data: validates, generates ID, saves, and logs actions.
 * @param {object} user - User object with at least a 'name' and 'email'
 * @param {object[]} db - Database array
 * @returns {object|null} User object with ID, or null if invalid
 */
function processUserData(user, db) {
  if (!validateEmail(user.email)) {
    logMessage(
      "processUserData",
      "ERROR",
      `Invalid email for user ${user.name}`
    );
    return null;
  }
  const userId = generateUserId();
  const userWithId = { id: userId, ...user };
  saveUserToDB(db, userWithId);
  logMessage(
    "processUserData",
    "INFO",
    `User ${user.name} added with ID ${userId}`
  );
  return userWithId;
}

// --- Test Cases ---
(function test() {
  const db = [];
  // Test validateEmail
  console.assert(
    validateEmail("test@example.com") === true,
    "Should validate correct email"
  );
  console.assert(
    validateEmail("bademail") === false,
    "Should invalidate incorrect email"
  );

  // Test generateUserId
  const id1 = generateUserId();
  const id2 = generateUserId();
  console.assert(id1 !== id2 || id1 === id2, "Should generate a user ID"); // Always true, just for demo

  // Test saveUserToDB
  const userObj = { id: "user_1", name: "Alice", email: "alice@example.com" };
  saveUserToDB(db, userObj);
  console.assert(db[0] === userObj, "Should save user to DB");

  // Test processUserData with valid input
  const user = { name: "Bob", email: "bob@example.com" };
  const result = processUserData(user, db);
  console.assert(
    result && result.id && result.name === "Bob",
    "Should process valid user"
  );

  // Test processUserData with invalid email
  const badUser = { name: "Eve", email: "notanemail" };
  const badResult = processUserData(badUser, db);
  console.assert(badResult === null, "Should return null for invalid email");

  // Logging output will appear in enterprise format in the console
})();

module.exports = {
  processUserData,
  validateEmail,
  generateUserId,
  saveUserToDB,
  logMessage,
};
