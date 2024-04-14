from rest_framework.response import Response
from .serializers import BookSerializer
from .models import Book
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class CreateBook(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)


class GetBooks(APIView):
    def get(self,request):
        if request.query_params:
            if request.query_params.get('author'):
                books = Book.objects.filter(author__icontains=request.query_params.get('author'))
                serializer = BookSerializer(books, many=True)
                if serializer.data:
                    return Response(serializer.data)
                else:
                    return Response(status= status.HTTP_404_NOT_FOUND)
            elif request.query_params.get('publisher'):
                books = Book.objects.filter(publisher_name__icontains=request.query_params.get('publisher'))
                serializer = BookSerializer(books, many=True)
                if serializer.data:
                    return Response(serializer.data)
                else:
                    return Response(status= status.HTTP_404_NOT_FOUND)
        else:
            book = Book.objects.all()
            serializer = BookSerializer(book, many=True)
            if serializer.data:
                return Response(serializer.data)
            else:
                return Response(status= status.HTTP_404_NOT_FOUND)


class DeleteBook(APIView):
    def delete(self,request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT) 
        except:
            return Response(status= status.HTTP_404_NOT_FOUND)