#include<windows.h>
#include<stdio.h>
#include<GL/gl.h>
#include<GL/glu.h>
#include<GL/glut.h>
#include<stdlib.h>
#include<string.h>
#include<stdio.h>
#include<conio.h>
#include <assert.h>
#include <fstream>
#include "imageloader.h"
int grid[13][11];
int slidev=0,slideh=0,slidehp=0,slidehn=0,slidevp=0,slidevn=0,win=0,loss=0,dex=1,windex=1,windexcount=1,dexcount=1;
float cx=5,cy=12;
void display();


//Makes the image into a texture, and returns the id of the texture
GLuint loadTexture(Image* image) {
	GLuint textureId;
	glGenTextures(1, &textureId); //Make room for our texture
	glBindTexture(GL_TEXTURE_2D, textureId); //Tell OpenGL which texture to edit
	//Map the image to the texture
	glTexImage2D(GL_TEXTURE_2D,                //Always GL_TEXTURE_2D
				 0,                            //0 for now
				 GL_RGB,                       //Format OpenGL uses for image
				 image->width, image->height,  //Width and height
				 0,                            //The border of the image
				 GL_RGB, //GL_RGB, because pixels are stored in RGB format
				 GL_UNSIGNED_BYTE, //GL_UNSIGNED_BYTE, because pixels are stored
				                   //as unsigned numbers
				 image->pixels);               //The actual pixel data
	return textureId; //Returns the id of the texture
}

GLuint _textureId; //The id of the texture
GLuint _textureId2;
GLuint _textureId3;
GLuint _textureId4;


void drawStrokeText(char*string,int x,int y,int z)
{
char *c;
glPushMatrix();
glTranslatef(x, y+8,z);
glScalef(0.40,0.40,z);
for (c=string; *c != '\0'; c++)
{
glutStrokeCharacter(GLUT_STROKE_ROMAN , *c);
}
glPopMatrix();
}

void make_grid()
{
    /*maze in grid */
    grid[0][8]=1;    grid[0][10]=1;
    grid[1][1]=1;    grid[1][2]=1;    grid[1][3]=1;    grid[1][5]=1;    grid[1][6]=1;
    grid[3][1]=1;    grid[3][3]=1;    grid[3][4]=1;    grid[3][5]=1;    grid[3][6]=1;    grid[3][9]=1;
    grid[5][0]=1;    grid[5][3]=1;    grid[5][5]=1;    grid[5][6]=1;    grid[5][9]=1;
    grid[6][3]=1;    grid[6][6]=1;    grid[6][7]=1;
    grid[7][3]=1;    grid[7][4]=1;    grid[7][6]=1;    grid[7][9]=1;
    grid[8][1]=1;    grid[8][9]=1;    grid[9][1]=1;
    grid[9][2]=1;    grid[9][4]=1;    grid[9][5]=1;    grid[9][7]=1;
    grid[10][1]=1;    grid[10][7]=1;    grid[10][8]=1;    grid[10][9]=1;
    grid[11][1]=1;    grid[11][3]=1;    grid[11][6]=1;    grid[11][7]=1;    grid[11][8]=1;    grid[11][9]=1;
    grid[12][3]=1;
    /* death traps */
    grid[0][6]=2;      grid[2][10]=2;      grid[12][4]=2;    grid[10][6]=2;
    /* final state */
    grid[0][10]=3;
    /*intial state */
    grid[11][5]=4;
}


void init()
{
     glEnable(GL_BLEND);
     glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0,550,0,650);
    Image* image = loadBMP("dexter.bmp");
	_textureId = loadTexture(image);
	delete image;
    Image* image2 = loadBMP("dexter2.bmp");
	_textureId2 = loadTexture(image2);//dexter hands stretched
	delete image2;
	Image* image3 = loadBMP("dexter3.bmp");
	_textureId3 = loadTexture(image3);//dexter hands stretched
	delete image3;
	Image* image4 = loadBMP("dexter4.bmp");
	_textureId4 = loadTexture(image4);//dexter hands stretched
	delete image4;
}

void animatepx()
{

     cx+=.25;
     if(slideh==0)
     cx-=.25;
     if(grid[int(cy)][int(cx+.75)]==1)
     {cx-=.25;
     slideh=0;
     slidehp=0;
     }
     if(cx>10)
     {
     cx-=.25;
     slideh=0;
     slidehp=0;
     }
     glutPostRedisplay();
     }

void animatenx()
{

     cx-=.25;
     if(slideh==0)
     cx+=.25;
     if(grid[int(cy)][int(cx)]==1)
     {cx+=.25;
     slideh=0;
     slidehn=0;
     }
     if(cx<0)
     {
     cx+=.25;
     slideh=0;
     slidehn=0;
     }
     glutPostRedisplay();
     }


void animatepy()
{

     cy+=.25;
     if(slidev==0)
     cy-=.25;
     if(grid[int(cy+.75)][int(cx)]==1)
     {cy-=.25;
     slidev=0;
     slidevp=0;
     }
     if(cy>12)
     {
     cy-=.25;
     slidev=0;
     slidevp=0;
     }

     glutPostRedisplay();
     }

void animateny()
{

     cy-=.25;
     if(slidev==0)
     cy+=.25;
     if(grid[int(cy)][int(cx)]==1)
     {cy+=.25;
     slidev=0;
     slidevn=0;
     }
     if(cy<0)
     {
     cy+=.25;
     slidev=0;
     slidevn=0;
     }
     glutPostRedisplay();
     }

void keyboard(unsigned char key, int x, int y)
{
switch (key) {
case 'd':
     if(!(win || loss))
     {
     if(slidev==0)
     slideh=1;
     if(slideh==1 && slidev==0 && slidehn==0)
     {
     slidehp=1;
     glutIdleFunc(animatepx);
     }
     }
break;
case 'a':
     if(!(win || loss))
      {  if(slidev==0)
     slideh=1;
     if(slideh==1 && slidev==0 && slidehp==0)
     {
     slidehn=1;
     glutIdleFunc(animatenx);
     }
     }
break;
case 'w':
     if(!(win || loss))
     {
     if(slideh==0)
     slidev=1;
     if(slidev==1 && slideh==0 && slidevn==0)
     {
     slidevp=1;
     glutIdleFunc(animatepy);
     }
     }
break;
case 's':
     if(!(win || loss))
     {
        if(slideh==0)
     slidev=1;
     if(slidev==1 && slideh==0 && slidevp==0)
     {
     slidevn=1;
     glutIdleFunc(animateny);
     }
     }
break;
case 'r':
     if(win || loss)
     {
     slideh=0;
     slidev=0;
     slidehn=0;
     slidehp=0;
     slidevp=0;
     slidevn=0;
     cx=5;
     cy=12;
     win=0;
     loss=0;
     dexcount=1;
     dex=1;
     }
break;
case 'e':
exit(0);
break;

}
}



void display()
{
    int i,x,y,l=0,w=0;
    glClearColor(0.2,0.3,0.4,0.5);
    glClear(GL_COLOR_BUFFER_BIT);
    glColor3f(1.0,1.0,1.0);
    glLineWidth(2.0);
    glLineStipple(2,0x5555);
    glEnable(GL_LINE_STIPPLE);
    glBegin(GL_LINES);
        for(i=0;i<=11;i++)
        {
            glVertex2d(50*i,0);
            glVertex2d(50*i,650);
        }
        for(i=0;i<=13;i++)
        {
            glVertex2d(0,50*i);
            glVertex2d(550,50*i);
        }
    glEnd();
    glColor3f(1.0,1.0,0.5);
    for(y=0;y<13;y++)
    {
                     for(x=0;x<11;x++)
                     {
                                      if(grid[y][x]==1)
                                      {
                                                       glRectd((x*50),(y*50),(x*50)+50,(y*50)+50);
                                                       }
                                      }
                     }

    glLineWidth(3.0);
    glColor3f(1.0,0.0,0.0);
    for(y=0;y<13;y++)
    {
                     for(x=0;x<11;x++)
                     {
                     if(grid[y][x]==2)
                     {
                            glBegin(GL_LINES);
                            glVertex2d(x*50,y*50)  ;
                            glVertex2d(x*50+50,y*50+50);
                            glVertex2d(x*50,y*50+50);
                            glVertex2d(x*50+50,y*50);
                            glEnd();
                            }
                                      }
                     }
    glColor3f(0.0,1.0,0.0);
    for(y=0;y<13;y++)
    {
                     for(x=0;x<11;x++)
                     {
                     if(grid[y][x]==3)
                     {
                            glBegin(GL_LINES);
                            glVertex2d(x*50,y*50)  ;
                            glVertex2d(x*50+50,y*50+50);
                            glVertex2d(x*50,y*50+50);
                            glVertex2d(x*50+50,y*50);
                            glEnd();
                            }
                                      }
                     }
    //glColor3f(1.0,0.0,0.0);
    //glRectd((cx*50),(cy*50),(cx*50)+50,(cy*50)+50);
    glColor3f(1.0,1.0,1.0);
    glEnable(GL_TEXTURE_2D);
    if(slideh == 1 || slidev == 1)
    {
              if(dexcount==4)
              {
              dex=!dex;
              }
              if(dexcount==4)
              {
                             dexcount=1;
                             }
              dexcount++;
              }
    else
    {
        dex=1;
        dexcount=1;
        }
    if(dex)
    {
	glBindTexture(GL_TEXTURE_2D, _textureId);
    }
    else
    {
        glBindTexture(GL_TEXTURE_2D, _textureId2);
        }
    if(win)
    {
          if(windexcount==8)
              {
              windex=!windex;
              }
              if(windexcount==8)
              {
                             windexcount=1;
                             }

           if(windex)
           {
                  glBindTexture(GL_TEXTURE_2D, _textureId4);

                  }
           else
           {
               glBindTexture(GL_TEXTURE_2D, _textureId3);
               }
           windexcount++;
           //windex=!windex;

           }
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
	//glColor3f(1.0f, 0.2f, 0.2f);
	glBegin(GL_QUADS);
	glTexCoord2f(0.0f, 0.0f);
	glVertex3f(cx*50,cy*50, 0.0f);
	glTexCoord2f(0.0f, 1.0f);
	glVertex3f(cx*50,cy*50+50, 0.0f);
	glTexCoord2f(1.0f, 1.0f);
	glVertex3f(cx*50+50,cy*50+50, 0.0f);
	glTexCoord2f(1.0f, 0.0f);
	glVertex3f(cx*50+50,cy*50, 0.0f);

	glEnd();
	glDisable(GL_TEXTURE_2D);
    /*glColor3f(1.0,1.0,1.0);
    glEnable(GL_TEXTURE_2D);
	glBindTexture(GL_TEXTURE_2D, _textureId);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
	//glColor3f(1.0f, 0.2f, 0.2f);
	glBegin(GL_QUADS);
	glTexCoord2f(0.0f, 0.0f);
	glVertex3f(10.0f,10.0f, 0.0f);
	glTexCoord2f(0.0f, 1.0f);
	glVertex3f(10.0f, 60.0f, 0.0f);
	glTexCoord2f(1.0f, 1.0f);
	glVertex3f(60.0f, 60.0f, -0.0f);
	glTexCoord2f(1.0f, 0.0f);
	glVertex3f(60.0f, 10.0f, 0.0f);

	glEnd();
	glDisable(GL_TEXTURE_2D);*/

    if(slidevn || slidehn)
    {
               l=(grid[int(cy+.75)][int(cx+.75)]==2);
               }
    if(slidevp || slidehp)
    {
               l=(grid[int(cy)][int(cx)]==2);
               }
    if(l)
    {
                       slidev=0;
                       slideh=0;
                       loss=1;
                       glColor4f(0.0, 0.0, 0.0, 0.3);
                       for(y=0;y<13;y++)
                       {
                     for(x=0;x<11;x++)
                     {
                        glRectd((x*50),(y*50),(x*50)+50,(y*50)+50);
                        }
                     }
                       glColor3f(1.0,0.0,0.0);
                       glLineWidth(4.0);
                       drawStrokeText("YOU LOOSE",125,350,0);
                       }

    if(slidevn || slidehn)
    {
               w=(grid[int(cy+.75)][int(cx+.75)]==3);
               }
    if(slidevp || slidehp)
    {
               w=(grid[int(cy)][int(cx)]==3);
               }

        if(w)
    {
                       slidev=0;
                       slideh=0;
                       win=1;
                       glColor4f(0.0, 0.0, 0.0, 0.3);
                       for(y=0;y<13;y++)
                       {
                     for(x=0;x<11;x++)
                     {
                        glRectd((x*50),(y*50),(x*50)+50,(y*50)+50);
                        }
                     }

                       glColor3f(0.0,1.0,0.0);

                       drawStrokeText("YOU WIN",150,350,0);
                       }
    Sleep(30);
    glutSwapBuffers();
}
void reshape(int w, int h)
{
    glViewport(0,0,(GLsizei)w,(GLsizei)h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D (0.0, (GLdouble) w, 0.0, (GLdouble) h);
}
int main(int argc, char** argv)
{

    make_grid();
    glutInit(&argc,argv);
    glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB);
    glutInitWindowPosition(50,50);
    glutInitWindowSize(550,650);
    glutCreateWindow("FrICtiOnLeSs");
    init();
    glutDisplayFunc(display);
    glutReshapeFunc(reshape);
    glutKeyboardFunc(keyboard);
    glutMainLoop();
    return 0;
}
