from marshmallow import Schema, fields, validate

class GradeAssignmentSchema(Schema):
    id = fields.Int(required=True)
    grade = fields.Str(required=True, validate=validate.OneOf(["A", "B", "C", "D", "E", "F"]))
