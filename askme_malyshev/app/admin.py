from django.contrib import admin
import app.models

# Register your models here.

admin.site.register(app.models.UserProfileModel)
admin.site.register(app.models.TagModel)
admin.site.register(app.models.QuestionModel)
admin.site.register(app.models.AnswerModel)
admin.site.register(app.models.LikeModel)
