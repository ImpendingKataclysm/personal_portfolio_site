/* Show Skills sections when their headings are clicked */

const keySkillHeading = document.getElementById("keySkillHeading");
const keySkillCol = document.getElementById("keySkills");
const codingSkillHeading = document.getElementById("codingSkillHeading");
const codingSkillCol = document.getElementById("codingSkills");

keySkillHeading.addEventListener('click', () => {
    keySkillCol.classList.toggle('show');
    codingSkillCol.classList.remove('show');
})

codingSkillHeading.addEventListener('click', () => {
    codingSkillCol.classList.toggle('show');
    keySkillCol.classList.remove('show');
})
