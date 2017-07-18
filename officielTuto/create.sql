BEGIN;
  --
  -- Create model Choice
  --
  CREATE TABLE "polls_choice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "choice_text" varchar(255) NOT NULL, "votes" integer NOT NULL);
  --
  -- Create model Question
  --
  CREATE TABLE "polls_question" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "question_text" varchar
  (255) NOT NULL, "pub_date" datetime NOT NULL);
  --
  -- Add field question to choice
  --
  ALTER TABLE "polls_choice" RENAME TO "polls_choice__old";
CREATE TABLE "polls_choice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "choice_text" varchar
(255) NOT NULL, "votes" integer NOT NULL, "question_id" integer NOT NULL REFERENCES "polls_question"("id")
)
;
INSERT INTO "polls_choice"
  ("votes", "id", "question_id", "choice_text")
SELECT "votes", "id", NULL, "choice_text"
FROM "polls_choice__old";
DROP TABLE "polls_choice__old";
CREATE INDEX "polls_choice_question_id_c5b4b260" ON "polls_choice" ("question_id");
COMMIT;
